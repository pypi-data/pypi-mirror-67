# Generated by Django 3.0.5 on 2020-04-27 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinpayments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PinPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment', models.CharField(blank=True, db_index=True, help_text='The name of the Pin environment to use, eg test or live.', max_length=25)),
                ('plan_token', models.CharField(blank=True, db_index=True, help_text='Unique ID from Pin for this plan', max_length=100, null=True, verbose_name='Pin API Plan Token')),
                ('active', models.BooleanField(blank=True, default=True, help_text='Is this Plan still visible on the Pin API?')),
                ('name', models.CharField(blank=True, help_text='Description as shown on statement', max_length=100, null=True)),
                ('currency', models.CharField(help_text='Currency of plan', max_length=10)),
                ('amount', models.IntegerField(help_text='Charge amount, in the base unit of the currency (e.g.: cents for AUD, yen for JPY)')),
                ('interval', models.IntegerField(help_text='The interval between subsequent charges, interpreted in units defined in interval_units')),
                ('interval_unit', models.CharField(choices=[('day', 'Day(s)'), ('week', 'Week(s)'), ('month', 'Month(s)'), ('year', 'Year(s)')], help_text='The unit of measure applied to the interval amount.', max_length=10)),
                ('intervals', models.IntegerField(blank=True, default=0, help_text='Number of intervals before a subscription is automatically cancelled. Default 0 (no limit)')),
                ('setup_amount', models.IntegerField(blank=True, default=0, help_text='Amount to charge (in the currency base unit, eg cents for AUD) at the start of the first full interval.')),
                ('trial_amount', models.IntegerField(blank=True, default=0, help_text='Amount the customer will be charged in the currency base unit upon initiating a trial of this plan.')),
                ('trial_interval', models.IntegerField(blank=True, default=0, help_text='The interval between the start of the trial period and beginning of the paid subscription proper.')),
                ('trial_interval_unit', models.CharField(choices=[('day', 'Day(s)'), ('week', 'Week(s)'), ('month', 'Month(s)'), ('year', 'Year(s)')], help_text='The unit of measure applied to the trial interval amount.', max_length=10)),
                ('permission_cancel', models.BooleanField(blank=True, default=True, help_text='Can the customer cancel the subscription themselves via a link in their receipts?')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pin_response_text', models.TextField(blank=True, help_text='The full JSON response from the Pin API', null=True, verbose_name='Complete API Response')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_token', models.CharField(blank=True, db_index=True, help_text='Unique ID from Pin for this subscription', max_length=100, null=True, verbose_name='Pin API Subscription Token')),
                ('environment', models.CharField(blank=True, db_index=True, help_text='The name of the Pin environment to use, eg test or live.', max_length=25)),
                ('active', models.BooleanField(blank=True, default=True, help_text='Is this subscription still visible on the Pin API?')),
                ('next_billing_date', models.DateTimeField(blank=True, help_text='The next time this subscription will be charged', null=True)),
                ('active_interval_started_at', models.DateTimeField(blank=True, help_text='When did the current trial or billing period begin?', null=True)),
                ('active_interval_finishes_at', models.DateTimeField(blank=True, help_text='When will the current trial or billing period finish?', null=True)),
                ('cancelled_at', models.DateTimeField(blank=True, help_text='When was the subscription cancelled?', null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinpayments.CustomerToken')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinpayments.PinPlan')),
            ],
        ),
    ]
