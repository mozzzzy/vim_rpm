# vim_rpm
Config files to build rpm packages of vim.

## Build
### Get source code of vim
```bash
$ git submodule update --init
```

### Build rpm packages
```bash
$ make all
```
Then the rpm packages are created in `rpmbuild/RPMS/x86_64` and `rpmbuild/SRPMS`.
```bash
$ tree rpmbuild -I BUILD
rpmbuild
├── BUILDROOT
├── RPMS
│   └── x86_64
│       ├── vim-8.2-1976.el7.x86_64.rpm
│       └── vim-debuginfo-8.2-1976.el7.x86_64.rpm
├── SOURCES
│   └── vim-8.2.tar.gz
├── SPECS
│   └── vim.spec
└── SRPMS
    └── vim-8.2-1976.el7.src.rpm

    6 directories, 5 files
```
