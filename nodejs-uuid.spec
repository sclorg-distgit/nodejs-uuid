%{?scl:%scl_package nodejs-uuid}
%{!?scl:%global pkg_name %{name}}

%global npm_name uuid
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-uuid
Version:	2.0.1
Release:	8%{?dist}
Summary:	Rigorous implementation of RFC4122 (v1 and v4) UUIDs.
Url:		https://github.com/shtylman/node-uuid
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	npm(mocha)
%endif

%description
Rigorous implementation of RFC4122 (v1 and v4) UUIDs.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
mocha test/test.js
%endif

%files
%{nodejs_sitelib}/uuid

%doc README.md
%license LICENSE.md

%changelog
* Mon May 02 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.1-8
- New specfile, remove redundant dependency

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.1-7
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.1-6
- Rebuilt with updated metapackage

* Fri Jan 15 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.1-5
- Fix dependency on uuid-js

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.1-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 2.0.1-1
- Initial package
