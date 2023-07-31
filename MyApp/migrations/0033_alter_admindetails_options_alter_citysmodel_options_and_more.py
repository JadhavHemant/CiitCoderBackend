# Generated by Django 4.2.1 on 2023-07-31 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0032_alter_contentmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admindetails',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='citysmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='codepostmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='commentpostmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='commentpostreplymodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='designationmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='experiancedetailsmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='gendermodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='jobopeningsmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='likessharespostmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='locationmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='postcategories',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='postcomment',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='postcommentreplymodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='postcommentreplys',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='postcommentsmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='postdislikemodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='postlikesdislikesmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='postlikesdislikestbmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='postlikessharesmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='postlikessharestablemodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='qualificationmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='qualimodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='rolemodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='specializationmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='statesmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='updatemodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='userdetailsmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='userpostmodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='userprofessionalexpertisemodel',
            options={'ordering': ('id',)},
        ),
    ]