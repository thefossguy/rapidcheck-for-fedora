%define git_commit ff6af6fc683159deb51c543b065eba14dfcf329b
%define git_short  ff6af6f

Name:           rapidcheck
Version:        0.0.0
Release:        1.%{git_short}%{?dist}
Summary:        QuickCheck clone for C++

License:        BSD-2-Clause
URL:            https://github.com/emil-e/rapidcheck
Source0:        https://github.com/emil-e/rapidcheck/archive/%{git_commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  cmake-data
BuildRequires:  ninja-build
BuildRequires:  gcc-g++

%description
RapidCheck is a C++ framework for property based testing inspired by
QuickCheck and other similar frameworks. In property based testing, you state
facts about your code that given certain precondition should always be true.
RapidCheck then generates random test data to try and find a case for which
the property doesn't hold. If such a case is found, RapidCheck tries to find
the smallest case (for some definition of smallest) for which the property
is still false and then displays this as a counterexample.

%package     -n rapidcheck-devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       gtest-devel # because this package produces a `rapidcheck_gtest`
Requires:       rapidcheck = %{version}-%{release}
%description -n rapidcheck-devel
This package contains the development files for %{name}.

%prep
%setup -n rapidcheck-%{git_commit}

%build
%cmake -DBUILD_SHARED_LIBS=ON -DRC_INSTALL_ALL_EXTRAS=ON
%cmake_build

%install
%cmake_install
tree %{buildroot}

%files
%exclude /usr/share
%{_includedir}/rapidcheck.h
%{_includedir}/rapidcheck/*
%{_libdir}/librapidcheck.so

%files -n rapidcheck-devel
%{_libdir}/librapidcheck.so
%{_libdir}/pkgconfig/rapidcheck.pc
%{_libdir}/pkgconfig/rapidcheck_boost.pc
%{_libdir}/pkgconfig/rapidcheck_boost_test.pc
%{_libdir}/pkgconfig/rapidcheck_catch.pc
%{_libdir}/pkgconfig/rapidcheck_doctest.pc
%{_libdir}/pkgconfig/rapidcheck_gtest.pc

%changelog

* Sat Feb 24 2024 Pratham Patel <thefirst1322@gmail.com> - 0.0.0-1.ff6af6f
- Initial packaging
