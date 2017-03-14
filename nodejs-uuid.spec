%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global npm_name uuid

# Disable until dependencies are met
%global enable_tests 0

Summary:       Rigorous implementation of RFC4122 (v1 and v4) UUIDs
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.0.1
Release:       7%{?dist}
License:       MIT
URL:           https://github.com/shtylman/node-uuid
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
BuildArch:     noarch

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
BuildRequires:  %{?scl_prefix}npm(coveralls)
%endif

%description
Simple, fast generation of RFC4122 UUIDS.

Features:
 - Generate RFC4122 version 1 or version 4 UUIDs
 - Runs in node.js and all browsers.
 - Cryptographically strong random # generation on supporting platforms
 - 1185 bytes minified and gzip'ed
 - Annotated source code

%prep
%setup -q -n package
%nodejs_fixdep uuid-js '0.7.5'

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr *.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha test/test.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc benchmark README.md
%doc LICENSE.md
%{nodejs_sitelib}/%{npm_name}

%changelog
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
