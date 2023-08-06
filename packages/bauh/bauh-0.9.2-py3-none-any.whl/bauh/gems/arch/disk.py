import json
import os
import re
from pathlib import Path
from typing import List, Dict, Iterable

from bauh.gems.arch import pacman
from bauh.gems.arch.model import ArchPackage

RE_DESKTOP_ENTRY = re.compile(r'(Exec|Icon|NoDisplay)\s*=\s*(.+)')
RE_CLEAN_NAME = re.compile(r'[+*?%]')


def write(pkg: ArchPackage):
    data = pkg.get_data_to_cache()

    if data:
        Path(pkg.get_disk_cache_path()).mkdir(parents=True, exist_ok=True)

        with open(pkg.get_disk_data_path(), 'w+') as f:
            f.write(json.dumps(data))


def fill_icon_path(pkg: ArchPackage, icon_paths: List[str], only_exact_match: bool):
    clean_name = RE_CLEAN_NAME.sub('', pkg.name)
    ends_with = re.compile(r'.+/{}\.(png|svg|xpm)$'.format(pkg.icon_path if pkg.icon_path else clean_name), re.IGNORECASE)

    for path in icon_paths:
        if ends_with.match(path):
            pkg.icon_path = path
            return

    if not only_exact_match:
        pkg_icons_path = pacman.list_icon_paths({pkg.name})

        if pkg_icons_path:
            pkg.set_icon(pkg_icons_path)


def set_icon_path(pkg: ArchPackage, icon_name: str = None):
    installed_icons = pacman.list_icon_paths({pkg.name})

    if installed_icons:
        exact_match = re.compile(r'.+/{}\..+$'.format(icon_name.split('.')[0] if icon_name else pkg.name))
        for icon_path in installed_icons:
            if exact_match.match(icon_path):
                pkg.icon_path = icon_path
                break


def save_several(pkgnames: Iterable[str], repo_map: Dict[str, str], overwrite: bool = True, maintainer: str = None,
                 categories: dict = None, when_prepared=None, after_written=None) -> int:
    if overwrite:
        to_cache = pkgnames
    else:
        to_cache = {n for n in pkgnames if not os.path.exists(ArchPackage.disk_cache_path(n))}

    desktop_files = pacman.list_desktop_entries(to_cache)

    no_desktop_files = set()

    to_write = []

    if desktop_files:
        desktop_matches, no_exact_match = {}, set()
        for pkg in to_cache:  # first try to find exact matches
            try:
                clean_name = RE_CLEAN_NAME.sub('', pkg)
                ends_with = re.compile(r'/usr/share/applications/{}.desktop$'.format(clean_name), re.IGNORECASE)
            except:
                raise

            for f in desktop_files:
                if ends_with.match(f) and os.path.isfile(f):
                    desktop_matches[pkg] = f
                    break

            if pkg not in desktop_matches:
                no_exact_match.add(pkg)
        if no_exact_match:  # check every not matched app individually
            for pkg in no_exact_match:
                entries = pacman.list_desktop_entries({pkg})

                if entries:
                    if len(entries) > 1:
                        for e in entries:
                            if e.startswith('/usr/share/applications') and os.path.isfile(e):
                                desktop_matches[pkg] = e
                                break
                    else:
                        if os.path.isfile(entries[0]):
                            desktop_matches[pkg] = entries[0]

        if not desktop_matches:
            no_desktop_files = to_cache
        else:
            if len(desktop_matches) != len(to_cache):
                no_desktop_files = {p for p in to_cache if p not in desktop_matches}

            pkgs, apps_icons_noabspath = [], []

            for pkgname, file in desktop_matches.items():
                p = ArchPackage(name=pkgname, repository=repo_map.get(pkgname))

                with open(file) as f:
                    try:
                        desktop_entry = f.read()
                        p.desktop_entry = file

                        for field in RE_DESKTOP_ENTRY.findall(desktop_entry):
                            if field[0] == 'Exec':
                                p.command = field[1].strip().replace('"', '')
                            elif field[0] == 'Icon':
                                p.icon_path = field[1].strip()

                                if p.icon_path and '/' not in p.icon_path:  # if the icon full path is not defined
                                    apps_icons_noabspath.append(p)
                            elif field[0] == 'NoDisplay' and field[1].strip().lower() == 'true':
                                p.command = None

                                if p.icon_path:
                                    apps_icons_noabspath.remove(p.icon_path)
                                    p.icon_path = None
                    except:
                        continue

                pkgs.append(p)

                if when_prepared:
                    when_prepared(p.name)

            if apps_icons_noabspath:
                icon_paths = pacman.list_icon_paths({app.name for app in apps_icons_noabspath})
                if icon_paths:
                    for p in apps_icons_noabspath:
                        fill_icon_path(p, icon_paths, False)

            for p in pkgs:
                to_write.append(p)
    else:
        no_desktop_files = {*pkgnames}

    if no_desktop_files:
        bin_paths = pacman.list_bin_paths(no_desktop_files)
        icon_paths = pacman.list_icon_paths(no_desktop_files)

        for n in no_desktop_files:
            p = ArchPackage(name=n, repository=repo_map.get(n))

            if bin_paths:
                clean_name = RE_CLEAN_NAME.sub('', p.name)
                ends_with = re.compile(r'.+/{}$'.format(clean_name), re.IGNORECASE)

                for path in bin_paths:
                    if ends_with.match(path):
                        p.command = path
                        break
            if icon_paths:
                fill_icon_path(p, icon_paths, only_exact_match=True)

            to_write.append(p)

            if when_prepared:
                when_prepared(p.name)

    if to_write:
        written = set()
        for p in to_write:
            if categories:
                p.categories = categories.get(p.name)

            if maintainer and not p.maintainer:
                p.maintainer = maintainer

            write(p)

            if after_written:
                after_written(p.name)

            written.add(p.name)

        if len(to_write) != len(to_cache):
            for n in pkgnames:
                if n not in written:
                    Path(ArchPackage.disk_cache_path(n)).mkdir(parents=True, exist_ok=True)
                    if after_written:
                        after_written(n)

        return len(to_write)
    return 0
