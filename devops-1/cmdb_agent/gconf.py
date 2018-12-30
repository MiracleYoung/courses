class Config:
    pass


if __name__ == '__main__':
    import os

    setattr(Config, 'PROJECT_PATH', os.path.dirname(os.path.abspath(__file__)))