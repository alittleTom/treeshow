�ĵ�˵����
1.myweb��ʹ��django ���web��Ŀ��ʵ�ֲ�ѯ���ݿ������������Ա��ű���
2.ʹ�õļ�����django�Ĵ��ҳ��ʹ��bootstrap��bootstrap-table�����jquery�����
3.�����ǵ�һ�δ������ܶ�app������ϰʹ��
4.PyMySQL-master������mysqlʹ�õģ�mysqlò�ƿ���֮������django�����Ұ�װʧ�ܣ����Ծ��������ַ�ʽ�������������Լ������ݿ���Ҫ��setting��������DATABASES ={}
5.static�ļ������ҽ�����һ����ž�̬��Դ���ļ��У����js��css�ȣ�����Լ����徲̬�ļ�����Ҫ��setting������STATIC_URL = 'static/'��STATIC_ROOT = os.path.join(BASE_DIR, 'static') ����urls.py������urlpatterns =[]+static(settings.STATIC_URL, document_root = settings.STATIC_ROOT).
6.ҳ�涼������templates����
7.fileUploadTest��ʵ�����ϴ��ļ��������ļ����浽upload�ļ����£���·���������ݿ�
8.yxtest��ʵ�������ݿ����ɾ�Ĳ飬��������ÿ�����ܶ���ʹ�õ�ͳһģ�壬�����Ƿֱ����
���磺��������Ա��ű������ǵ�����������ʹ��һ��ģ�壬ͨ�������ö�������������ɽ��档
9. yxtest2��ʵ���˽�һ�����ݿ�ı���������ʽ��չʾ��ǰ���������ж�Ӧ�Ĺ�ϵ����
10.yxtest3��ʵ������������Ա��ű��������ݿ���ȡ����װ��json�����������ʹ��bootstrao-table��չʾ
���Ƕ�Ӧ����ɾ�Ĳ鶼��ʹ���ض���ģ�壨�ô����ǿ���չʾ�Լ���չʾ����Ϣ�����Ҷ���򵥣�
ע�⣺bootstrao-table�Լ���ajax���ܡ���ҳ���ʼ����ʱ����ʹ��ajax�ύ���󣬶����Ƿ���ģ���ʱ��˳�㷵�����󡣣�ps:ֻ�������ʵ�����������ܣ���������ơ��������ֻ�����˰�ť���¼�����û�ж��崦����̣�


django3.5��ʹ�õ����
1.python manage.py startapp APPname �½�һ��app
2.django1.9�Ժ�֧��python manage.py syncdb
����ʹ��python manage.py migrate ���� python manage.py makemigrations
3.�½���model�Ժ�ִ��
python manage.py makemigrations ����������ݿ������������ݿ�Ǩ���ļ� 
python manage.py sqlmigrate APPname 0001 ���������ݿ�Ǩ���ļ�ת�������ݿ����� 
python manage.py migrate ����ִ��Ǩ�ƶ���
