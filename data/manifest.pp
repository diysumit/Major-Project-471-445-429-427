# Class: data_download
#
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

#Clss: python
#
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
