Name:           vim
Version:        8.2
Release:        1976%{?dist}
Summary:        VIM editor built from github source codes.

License:        Vim
URL:            http://www.vim.org/
Source0:        vim-8.2.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
Requires: tcsh

%define _unpackaged_files_terminate_build 0

%description
VIM (VIsual editor iMproved) is an updated and improved version of the
vi editor.  Vi was the first real screen-based editor for UNIX, and is
still very popular.  VIM improves on vi by adding new features:
multiple windows, multi-level undo, block highlighting and more.

%prep
%setup -q -n vim


%build
./configure --prefix=/opt
make %{?_smp_mflags}


%install
%make_install


%files
/opt/bin/*
/opt/share/man/*
/opt/share/%{name}


%changelog
