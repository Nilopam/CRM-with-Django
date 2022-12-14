# Generated by Django 4.1 on 2022-09-05 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('guardian_name', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=50)),
                ('joining_Date', models.DateField()),
                ('emp_type', models.CharField(choices=[('leader', 'Team Leader'), ('employee', 'Normal Employee')], max_length=50)),
                ('mobile', models.CharField(max_length=14, unique=True)),
                ('corporate_mobile', models.CharField(blank=True, max_length=14, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('alternate_mobile', models.CharField(blank=True, max_length=14, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=50, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=50, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=50, null=True)),
                ('account_number', models.CharField(blank=True, max_length=50, null=True)),
                ('esi_number', models.CharField(blank=True, max_length=50, null=True)),
                ('pan', models.CharField(blank=True, max_length=50, null=True)),
                ('adhaar', models.CharField(blank=True, max_length=50, null=True)),
                ('vote', models.CharField(blank=True, max_length=50, null=True)),
                ('passport', models.CharField(blank=True, max_length=50, null=True)),
                ('belonging', models.TextField(blank=True, max_length=500, null=True)),
                ('gross_salary', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_salary', models.CharField(blank=True, max_length=50, null=True)),
                ('basic_salary', models.CharField(blank=True, max_length=50, null=True)),
                ('house_salary', models.CharField(blank=True, max_length=50, null=True)),
                ('education_salary', models.CharField(blank=True, max_length=50, null=True)),
                ('medical_salary', models.CharField(blank=True, max_length=50, null=True)),
                ('other_salary', models.CharField(blank=True, max_length=50, null=True)),
                ('esi_emp', models.CharField(blank=True, max_length=50, null=True)),
                ('esi_empr', models.CharField(blank=True, max_length=50, null=True)),
                ('esi_total', models.CharField(blank=True, max_length=50, null=True)),
                ('net_salary', models.CharField(blank=True, max_length=50, null=True)),
                ('monthly_ctc', models.CharField(blank=True, max_length=50, null=True)),
                ('yearly_ctc', models.CharField(blank=True, max_length=50, null=True)),
                ('education_doc', models.FileField(blank=True, null=True, upload_to='uploads/education/')),
                ('experience_doc', models.FileField(blank=True, null=True, upload_to='uploads/experience/')),
                ('pay_slip_doc', models.FileField(blank=True, null=True, upload_to='uploads/pay_slip/')),
                ('resignation_doc', models.FileField(blank=True, null=True, upload_to='uploads/resignation/')),
                ('photograph_doc', models.FileField(blank=True, null=True, upload_to='uploads/photograph/')),
                ('poi_doc', models.FileField(blank=True, null=True, upload_to='uploads/id_proof/')),
                ('poa_doc', models.FileField(blank=True, null=True, upload_to='uploads/education/')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.designation')),
                ('place_of_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.place')),
            ],
        ),
        migrations.CreateModel(
            name='Leaders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leadername', models.CharField(max_length=50)),
                ('leaderid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('notice_content', models.CharField(max_length=500)),
                ('attachment', models.FileField(upload_to='Notice')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TravelAllow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('from_where', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('distance', models.CharField(max_length=50)),
                ('expense', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('A', 'Approve'), ('R', 'Reject')], default='P', max_length=10)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.emp')),
            ],
        ),
        migrations.CreateModel(
            name='Resignation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('experience_letter', models.CharField(blank=True, max_length=50)),
                ('release_letter', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(choices=[('A', 'Approve'), ('R', 'Reject'), ('P', 'Pending')], default='P', max_length=1)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.emp')),
            ],
        ),
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.emp')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('category', models.CharField(choices=[('EL', 'EL'), ('CL', 'CL')], max_length=50)),
                ('reason', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('A', 'Approve'), ('R', 'Reject'), ('P', 'Pending')], default='P', max_length=50)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.emp')),
            ],
        ),
        migrations.AddField(
            model_name='emp',
            name='under_of',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.leaders'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('in_time', models.DateTimeField(blank=True, null=True)),
                ('out_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('A', 'Approve'), ('R', 'Reject')], default='A', max_length=50)),
                ('half', models.BooleanField(default=False)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.emp')),
            ],
        ),
    ]
