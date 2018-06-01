class Config:
    DEBUG = True
    # 配置数据库的连接
    SQLALCHEMY_DATABASE_URI = 'mysql://root:592613aa@localhost:3306/web_project'
    # 动态追踪修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 设置密钥
    SECRET_KEY = 'pKg1DPQfsI57kMkY1MeUrRqboIsDmPA+tF3Lsn8eETw='
    # 在请求过程中自动提交数据
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
