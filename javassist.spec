# TODO:
# - rename to java-javassist (?)
# - it doesn't build with gcj, because it requires com.sun.jdi. Is there any
#   non-sun package that provides these classes?

%include	/usr/lib/rpm/macros.java
Summary:	Java Programming Assistant: bytecode manipulation
Summary(pl.UTF-8):	Asystent programisty Javy: operacje na bajtkodzie
Name:		javassist
Version:	3.11.0
Release:	1
License:	MPL and LGPL
Group:		Libraries/Java
Source0:	http://dl.sourceforge.net/project/jboss/Javassist/3.11.0.GA/%{name}-3.11.GA.zip
# Source0-md5:	3afecb69a0c167a978c93f7074a74dfc
URL:		http://www.csg.is.titech.ac.jp/~chiba/javassist/
BuildRequires:	ant >= 0:1.6
BuildRequires:	jdk
BuildRequires:	jpackage-utils >= 0:1.6
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
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

%description -l pl.UTF-8
Javassist (asystent programisty Javy) ułatwia operacje na bajtkodzie
Javy. Jest to biblioteka klas do modyfikowania bajtkodu w Javie;
pozwala programom w Javie definiować nowe klasy w czasie działania
oraz modyfikować pliki klas w czasie wczytywania ich przez JVM. W
przeciwieństwie do innych podobnych edytorów bajtkodu Javassist
udostępnia dwa poziomy API: źródłowy i bajtkodu. Korzystający z API
poziomu źródłowego mogą modyfikować plik klasy bez znajomości
specyfikacji bajtkodu. Całe API jest zaprojektowane z użyciem
wyłącznie słownictwa języka Java. Można nawet określać wstawiany
bajtkod w postaci tekstu źródłowego - Javassist skompiluje go w locie.
Z drugiej strony API poziomu bajtkodu pozwala użytkownikom
bezpośrednio modyfikować pliki klas, tak jak inne edytory.

%package demo
Summary:	Samples for Javassist
Summary(pl.UTF-8):	Przykłady użycia Javassista
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for Javassist.

%description demo -l pl.UTF-8
Pliki demonstracyjne i przykłady dla Javassista.

%package javadoc
Summary:	Javadoc for Javassista
Summary(pl.UTF-8):	Dokumentacja Javadoc do Javassista
Group:		Documentation

%description javadoc
Documentation for Javassist.

%description javadoc -l fr.UTF-8
Javadoc pour Javassist.

%description javadoc -l pl.UTF-8
Dokumentacja do Javassista.

%package manual
Summary:	Tutorial for Javassist
Summary(pl.UTF-8):	Podręcznik do Javassista
Group:		Documentation

%description manual
Tutorial for Javassist.

%description manual -l pl.UTF-8
Podręcznik do Javassista.

%prep
%setup -q
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

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc License.html Readme.html
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
%doc tutorial
