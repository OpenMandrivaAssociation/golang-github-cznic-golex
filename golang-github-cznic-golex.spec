# https://github.com/cznic/golex
%global goipath github.com/cznic/golex
%global commit  4ab7c5e190e49208c823ce8ec803aa39e6a4b31a
%gometa

Name:           golang-github-cznic-golex
Version:        0
Release:        0.9%{?dist}
Summary:        Lex/Flex-like utility written in Go
License:        BSD

URL:            %{gourl}
Source0:        %{gosource}

Provides:       golex%{?_isa} = %{version}-%{release}

BuildRequires:  golang(github.com/cznic/lex)
BuildRequires:  golang(github.com/cznic/lexer)

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%build
%gobuildroot

%gobuild -o _bin/golex %{goipath}


%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 _bin/golex %{buildroot}%{_bindir}

%goinstall


%check
%gochecks


%files
%license LICENSE
%doc CONTRIBUTORS AUTHORS README
%{_bindir}/golex


%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTORS AUTHORS README


%changelog
* Thu Nov 15 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.9.20170803git4ab7c5e
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.8.20170803git4ab7c5e
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0-0.7.20170803git4ab7c5e
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20170803.git4ab7c5e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20170803.git4ab7c5e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.4.20170803.git4ab7c5e
- Bump to commit 4ab7c5e.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20170310.gitd7f6f2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20170310.gitd7f6f2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20170310.gitd7f6f2b
- First package for Fedora

