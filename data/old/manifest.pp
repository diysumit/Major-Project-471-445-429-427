# Class: data_download
# packages for downloading data
#
class data_download {
  # resources
  package {'kaggle':
    ensure => installed,
  }
  service {'kaggle':
    ensure => running,
  }
  package {'wget':
    ensure => latest,
  }
  service {'wget':
    ensure => running,
  }
}

# Class: python
# for installing python on system
#
class python {
  package {'python3':
    ensure => installed,
  }
  package{'python3-pip':
    ensure => installed,
  }
  service {'python3':
    ensure => running
  }
}

# Class: virtualenv
# for creating virtualenv
#
class virtualenv {
  # resources
  package {'virtualenv':
    ensure => installed;
  }
  service {'virtualenv':
    ensure => running;
  }
}

# Class: flutter_app
# all dependencies for flutter app
#
class flutter_app {
  # resources
  package {'dart':
    ensure => installed;
  }
  package{'flutter':
    ensure => installed;
  }
}
