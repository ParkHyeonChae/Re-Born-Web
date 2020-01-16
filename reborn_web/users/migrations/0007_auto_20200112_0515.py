# Generated by Django 3.0.1 on 2020-01-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200112_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='circles',
            field=models.CharField(choices=[('미가입', '미가입'), ('NUXPIA', 'NUXPIA'), ('NET', 'NET'), ('DOT-GABI', 'DOT-GABI'), ('IMAGINE', 'IMAGINE'), ('P&N', 'P&N'), ('MEGA-BRAIN', 'MEGA-BRAIN')], max_length=18, null=True, verbose_name='동아리'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('외부인', '학부생이 아님'), ('컴퓨터공학부', '컴퓨터공학부'), ('드론IOT시뮬레이션학부', '드론IOT시뮬레이션학부'), ('의과대학', '의과대학'), ('문리과대학', '문리과대학'), ('사회과학대학', '사회과학대학'), ('공과대학', '공과대학'), ('보건의료융합대학', '보건의료융합대학'), ('BNIT융합대학', 'BNIT융합대학'), ('약학대학', '약학대학')], max_length=24, null=True, verbose_name='학과'),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(choices=[('1학년', '1학년'), ('2학년', '2학년'), ('3학년', '3학년'), ('4학년', '4학년'), ('졸업생', '졸업생')], max_length=18, null=True, verbose_name='학년'),
        ),
    ]