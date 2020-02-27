# Generated by Django 3.0.2 on 2020-02-27 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(choices=[('first', '1학년'), ('second', '2학년'), ('third', '3학년'), ('fourth', '4학년')], max_length=10, verbose_name='학년')),
                ('subject', models.CharField(max_length=30, verbose_name='시험과목명')),
                ('professor', models.CharField(max_length=15, verbose_name='담당교수명')),
                ('day', models.CharField(choices=[('mon', '월요일'), ('tue', '화요일'), ('wed', '수요일'), ('thu', '목요일'), ('fri', '금요일'), ('sat', '토요일'), ('sun', '일요일')], max_length=30, verbose_name='시험요일')),
                ('date', models.DateField(null=True, verbose_name='시험날짜')),
                ('time', models.CharField(choices=[('1', '1교시(오전9시)'), ('2', '2교시(오전10시)'), ('3', '3교시(오전11시)'), ('4', '4교시(오후12시)'), ('5', '5교시(오후1시)'), ('6', '6교시(오후2시)'), ('7', '7교시(오후3시)'), ('8', '8교시(오후4시)'), ('9', '9교시(오후5시)'), ('10', '10교시(오후6시)'), ('11', '11교시(오후7시)'), ('12', '12교시(오후8시)')], max_length=30, verbose_name='시험시간')),
                ('time_length', models.CharField(choices=[('1', '1시간'), ('2', '2시간'), ('3', '3시간'), ('4', '4시간')], default=1, max_length=10, verbose_name='시험시간길이')),
                ('location', models.CharField(max_length=20, verbose_name='시험장소')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='수정일')),
            ],
            options={
                'verbose_name': '시험시간표',
                'verbose_name_plural': '시험시간표',
                'db_table': '시험시간표',
            },
        ),
    ]
