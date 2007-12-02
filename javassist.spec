%include	/usr/lib/rpm/macros.java
Summary:	Java Programming Assistant: bytecode manipulation
Name:		javassist
Version:	3.5
Release:	0.1
License:	MPL and LGPL
Group:		Development/Languages/Java
Source0:	http://repository.jboss.com/javassist/3.5.0.CR1-brew/src/%{name}-%{version}.CR1-src.tar.gz
# Source0-md5:	59d0c8858062b6ba6d738a1f41959d8b
URL:		http://www.csg.is.titech.ac.jp/~chiba/javassist/
BuildRequires:	ant >= 0:1.6
BuildRequires:	jpackage-utils >= 0:1.6
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Javassist (Java Programming Assistant) makes Java bytecode
manipulation simple. It is a class library for editing bytecodes in
Java; it enables Java programs to define a new class at runtime and to
modify a class file when the JVM loads it. Unlike other similar
bytecode editors, Javassist provides two levels of API: source level
and bytecode level. If the users use the source-level API, they can
edit a class file without knowledge of the specifications of the Java
bytecode. The whole API is designed with only the vocabulary of the
Java language. You can even specify inserted bytecode in the form of
source text; Javassist compiles it on the fly. On the other hand, the
bytecode-level API allows the users to directly edit a class file as
other editors.

%package demo
Summary:	Samples for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for %{name}.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla pakietu %{name}.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Documentation

%description javadoc
Documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{name} -

%description javadoc -l fr.UTF-8
Javadoc pour %{name}.

%package manual
Summary:	Tutorial for %{name}
Group:		Documentation

%description manual
Manual for %{name}.

%prep
%setup -q -n %{name}-%{version}.CR1-src
find -name '*.jar' | xargs rm -vf

%build
%ant dist

%install
rm -rf $RPM_BUILD_ROOT

# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# demo
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -pr sample/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr html/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

# manual
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/tutorial
cp -pr tutorial/* $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/tutorial
cp -p License.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/License.html
%{_javadir}/*.jar

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}

%files manual
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}/tutorial
