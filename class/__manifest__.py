{
    'name': "Quản lý học sinh lớp IT",
    'summary': """class model""",
    'description': """Quản lý điểm""",
    'author': "Thắng",
    'website': "https://www.youtube.com/channel/UCbWIUWKYllxp4WxbMDjs7JA",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
    'security/ir.model.access.csv',
    'views/my_class_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}