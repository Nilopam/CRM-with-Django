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
            name='GSTR2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Summary_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('sale_price', models.IntegerField()),
                ('purchase_price', models.IntegerField()),
                ('stock_qty', models.IntegerField()),
                ('stock_value', models.IntegerField()),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.product')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Sale_Return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bill_no', models.IntegerField()),
                ('total_sale', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('party_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.party')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Sale_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('invoice_no', models.IntegerField()),
                ('bill_type', models.CharField(max_length=200)),
                ('payment_status', models.CharField(max_length=300)),
                ('total_amount', models.IntegerField()),
                ('recieved_amount', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('party_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.party')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Sale_Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('subtotal_amount', models.IntegerField()),
                ('final_amount', models.IntegerField()),
                ('payment_type', models.CharField(max_length=30)),
                ('state_of_supply', models.CharField(choices=[('SELECT', 'Select'), ('ANDHRA PRADESH', 'Andhra Pradesh'), ('ASSAM', 'Assam'), ('BIHAR', 'Bihar'), ('CHHATTISGARH', 'Chhattisgarh'), ('GOA', 'Goa'), ('GUJRAT', 'Gujrat'), ('HARYANA', 'Haryana'), ('HIMACHAL PRADESH', 'Himachal Pradesh'), ('JHARKHAND', 'Jharkhand'), ('KARNATAKA', 'Karnataka'), ('KERALA', 'Kerala'), ('MADHYA PRADESH', 'Madhya Pradesh'), ('MAHARASHTRA', 'Maharashtra'), ('MANIPUR', 'Manipur'), ('MEGHALAYA', 'Meghalaya'), ('MIZORAM', 'Mizoram'), ('NAGALAND', 'Nagaland'), ('ODISHA', 'Odisha'), ('PUNJAB', 'Punjab'), ('RAJASTHAN', 'Rajasthan'), ('SIKKIM', 'Sikkim'), ('TAMILNADU', 'Tamilnadu'), ('TELENGANA', 'Telengana'), ('TRIPURA', 'Tripura'), ('UTTARAKHAND', 'Uttarakhand'), ('UTTAR PRADESH', 'Uttar pradesh'), ('WEST BENGAL', 'West bengal'), ('ANADAMAN & NICOBAR ISLANDS', 'Andaman & Nicobar Islands'), ('DADRA and NAGAR HAVELI and DAMAN & DIU', 'Dadra & Nagar Haveli and Daman & Diu'), ('JAMMU & KASHMIR', 'Jammu & Kashmir'), ('LAKSHADWEEP', 'Lakshadweep'), ('THE GOVERNMENT of NCT of DELHI', 'The Government of NCT of Delhi'), ('LADAKH', 'Ladakh'), ('PUDUCHERRY', 'Puducherry')], default='SELECT', max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('party_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.party')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Return',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bill_no', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('party_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.party')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('purchase_bill_no', models.IntegerField()),
                ('bill_type', models.CharField(max_length=200)),
                ('payment_status', models.CharField(max_length=300)),
                ('total_amount', models.IntegerField()),
                ('recieved_amount', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('party_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.party')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('bill_no', models.IntegerField()),
                ('subtotal_amount', models.IntegerField()),
                ('final_amount', models.IntegerField()),
                ('payment_type', models.CharField(max_length=30)),
                ('state_of_supply', models.CharField(choices=[('SELECT', 'Select'), ('ANDHRA PRADESH', 'Andhra Pradesh'), ('ASSAM', 'Assam'), ('BIHAR', 'Bihar'), ('CHHATTISGARH', 'Chhattisgarh'), ('GOA', 'Goa'), ('GUJRAT', 'Gujrat'), ('HARYANA', 'Haryana'), ('HIMACHAL PRADESH', 'Himachal Pradesh'), ('JHARKHAND', 'Jharkhand'), ('KARNATAKA', 'Karnataka'), ('KERALA', 'Kerala'), ('MADHYA PRADESH', 'Madhya Pradesh'), ('MAHARASHTRA', 'Maharashtra'), ('MANIPUR', 'Manipur'), ('MEGHALAYA', 'Meghalaya'), ('MIZORAM', 'Mizoram'), ('NAGALAND', 'Nagaland'), ('ODISHA', 'Odisha'), ('PUNJAB', 'Punjab'), ('RAJASTHAN', 'Rajasthan'), ('SIKKIM', 'Sikkim'), ('TAMILNADU', 'Tamilnadu'), ('TELENGANA', 'Telengana'), ('TRIPURA', 'Tripura'), ('UTTARAKHAND', 'Uttarakhand'), ('UTTAR PRADESH', 'Uttar pradesh'), ('WEST BENGAL', 'West bengal'), ('ANADAMAN & NICOBAR ISLANDS', 'Andaman & Nicobar Islands'), ('DADRA and NAGAR HAVELI and DAMAN & DIU', 'Dadra & Nagar Haveli and Daman & Diu'), ('JAMMU & KASHMIR', 'Jammu & Kashmir'), ('LAKSHADWEEP', 'Lakshadweep'), ('THE GOVERNMENT of NCT of DELHI', 'The Government of NCT of Delhi'), ('LADAKH', 'Ladakh'), ('PUDUCHERRY', 'Puducherry')], default='SELECT', max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('party_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.party')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Out',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('party_balance', models.IntegerField()),
                ('paid', models.IntegerField()),
                ('balance_due', models.IntegerField()),
                ('payment_type', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.bankaccount')),
                ('party_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.party')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_In',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('party_balance', models.IntegerField()),
                ('opening_balance', models.IntegerField()),
                ('recieved', models.IntegerField()),
                ('balance_due', models.IntegerField()),
                ('payment_type', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.bankaccount')),
                ('party_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.party')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='GSTR3B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('inter_state_supplies', models.CharField(max_length=200)),
                ('intra_state_supplies', models.CharField(max_length=200)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='GSTR1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hsn', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('uqc', models.CharField(max_length=300)),
                ('taxable_value', models.IntegerField()),
                ('integrated_tax_amount', models.IntegerField()),
                ('central_tax_amount', models.IntegerField()),
                ('state_ui_tax_amount', models.IntegerField()),
                ('cess_amount', models.IntegerField()),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('expense_category', models.CharField(max_length=200)),
                ('total_amount', models.IntegerField()),
                ('payment_type', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.bankaccount')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Due_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('invoice_no', models.IntegerField()),
                ('bill_type', models.CharField(max_length=200)),
                ('contact_details', models.IntegerField()),
                ('payment_status', models.CharField(max_length=300)),
                ('total_amount', models.IntegerField()),
                ('recieved_amount', models.IntegerField()),
                ('balance_amaount', models.IntegerField()),
                ('employee_name', models.CharField(max_length=200)),
                ('party_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.party')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Daybook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('invoice_no', models.IntegerField()),
                ('bill_type', models.CharField(max_length=200)),
                ('particulars', models.CharField(max_length=200)),
                ('debit', models.IntegerField()),
                ('credit', models.IntegerField()),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.accounting_year')),
            ],
        ),
        migrations.CreateModel(
            name='Add_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.product')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.service')),
            ],
        ),
    ]