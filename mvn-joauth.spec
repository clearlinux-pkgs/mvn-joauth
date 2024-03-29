#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-joauth
Version  : 6.0.2
Release  : 1
URL      : https://github.com/twitter/joauth/archive/joauth-6.0.2.tar.gz
Source0  : https://github.com/twitter/joauth/archive/joauth-6.0.2.tar.gz
Source1  : https://repo1.maven.org/maven2/com/twitter/joauth/6.0.2/joauth-6.0.2.jar
Source2  : https://repo1.maven.org/maven2/com/twitter/joauth/6.0.2/joauth-6.0.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-joauth-data = %{version}-%{release}
Requires: mvn-joauth-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
# JOAuth [![Build Status](https://travis-ci.org/twitter/joauth.png?branch=master)](https://travis-ci.org/twitter/joauth)

%package data
Summary: data components for the mvn-joauth package.
Group: Data

%description data
data components for the mvn-joauth package.


%package license
Summary: license components for the mvn-joauth package.
Group: Default

%description license
license components for the mvn-joauth package.


%prep
%setup -q -n joauth-joauth-6.0.2

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-joauth
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-joauth/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/joauth/6.0.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/twitter/joauth/6.0.2/joauth-6.0.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/twitter/joauth/6.0.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/twitter/joauth/6.0.2/joauth-6.0.2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/twitter/joauth/6.0.2/joauth-6.0.2.jar
/usr/share/java/.m2/repository/com/twitter/joauth/6.0.2/joauth-6.0.2.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-joauth/LICENSE
