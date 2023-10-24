# Generated by Django 4.2 on 2023-10-23 22:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Name')),
                ('note', models.CharField(default='No Note', max_length=50, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='brands', verbose_name='Image')),
                ('note', models.CharField(default='No Note', max_length=50, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone', models.CharField(max_length=50, unique=True, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('note', models.CharField(default='No Note', max_length=50, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Name')),
                ('note', models.CharField(default='No Note', max_length=50, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Name')),
                ('note', models.CharField(default='No Note', max_length=50, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Name')),
                ('note', models.CharField(default='No Note', max_length=50, verbose_name='Note')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Delivered', 'Delivered')], default=('Pending', 'Pending'), max_length=50, verbose_name='Status')),
                ('barcode', models.CharField(max_length=50, verbose_name='Barcode')),
                ('serial', models.CharField(max_length=50, unique=True, verbose_name='S.N')),
                ('des', models.CharField(max_length=200, verbose_name='Description')),
                ('active', models.CharField(choices=[('In_Active', 'In_Active'), ('Out_Active', 'Out_Active')], default=('In_Active', 'In_Active'), max_length=50, verbose_name='Active')),
                ('invoice', models.ImageField(blank=True, null=True, upload_to='Invoice', verbose_name='invoice')),
                ('purchase_date', models.DateField(blank=True, null=True, verbose_name='Purchase_Date')),
                ('iss_detail', models.TextField(default='Write Issue Detail', max_length=300, verbose_name='Detail')),
                ('received_date', models.DateField(default=django.utils.timezone.now, verbose_name='Received_Date')),
                ('act_detail', models.TextField(default='Write Action Detail', max_length=300, verbose_name='Detail')),
                ('delivery_date', models.DateField(blank=True, null=True, verbose_name='Delivery_Date')),
                ('note', models.CharField(default='No Note', max_length=50, verbose_name='Note')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_Action', to='CRM.action', verbose_name='Action')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_brand', to='CRM.brand', verbose_name='Brand')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_client', to='CRM.client', verbose_name='Client')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_color', to='CRM.color', verbose_name='Color')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_Company', to='CRM.company', verbose_name='Company')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_Issue', to='CRM.issue', verbose_name='Issue')),
            ],
        ),
        migrations.CreateModel(
            name='Follow_Up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connect', models.CharField(choices=[('Phone', 'Phone'), ('WatsApp', 'WatsApp'), ('Messenger', 'Messenger')], default=('Pending', 'Pending'), max_length=50, verbose_name='Connect')),
                ('rate', models.CharField(choices=[('راضى', 'راضى'), ('غير_راضى', 'غير_راضى'), ('يحتاج_تطوير', 'يحتاج_تطوير')], default=('راضى', 'راضى'), max_length=50, verbose_name='Rate')),
                ('comment', models.TextField(blank=True, max_length=300, null=True, verbose_name='Comment')),
                ('note', models.CharField(default='No Note', max_length=50, verbose_name='Note')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_Follow_Up', to='CRM.order', verbose_name='Order')),
            ],
        ),
    ]