Name: okio
Version: 1.4.0
Release: 1%{?dist}
Summary: A modern I/O API for Java

License: ASL 2.0
URL: https://github.com/square/okio
Source0: https://github.com/square/okio/archive/okio-parent-1.4.0.tar.gz
BuildArch: noarch

BuildRequires: maven-local

%description
Okio is a new library that complements java.io and java.nio to make it much
easier to access, store, and process your data.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n okio-okio-parent-%{version}

# Remove animal sniffer, missing dependency and not needed since Fedora 22+
# ships only with Java 8
find -name "*.java" -exec sed -i "/IgnoreJRERequirement/d" {} +

%pom_remove_dep org.codehaus.mojo:animal-sniffer-annotations okio
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin okio

# Missing dependency for benchmark, no need to ship benchmark artifacts
%pom_disable_module benchmarks

%build
# Network tests fails when running in mock
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc BUG-BOUNTY.md CONTRIBUTING.md CHANGELOG.md README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc BUG-BOUNTY.md CONTRIBUTING.md CHANGELOG.md README.md
%license LICENSE.txt

%changelog
* Wed Jun 17 2015 Jonny Heggheim <hegjon@gmail.com> - 1.4.0-1
- Inital packaging
