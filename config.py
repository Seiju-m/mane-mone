class ProdConfig(object):
    DEBUG = False
    TESTING = False
    DATABASE = 'postgresql'
    USER = 'rsownwafjdissl'
    PASSWORD = '04bbfe55fd79187e75d3256230844b9f0e4a2e396a40db8977e4e1e05760c177'
    HOST = 'ec2-34-230-149-169.compute-1.amazonaws.com'
    PORT = '5432'
    DB_NAME = 'dar8qtfcfi65mk'


class DevConfig(object):
    DEBUG = True
    TESTING = True
    DATABASE = 'postgresql'
    USER = 'postgres'
    PASSWORD = 'Seiju7479'
    HOST = '127.0.0.1'
    PORT = '5432'
    DB_NAME = 'manage3'