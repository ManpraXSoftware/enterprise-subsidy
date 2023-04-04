# Generated by Django 3.2.18 on 2023-04-04 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openedx_ledger', '0005_help_text_and_more_indices'),
        ('subsidy', '0015_revenue_category_field_20230331_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubsidy',
            name='ledger',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The one Ledger uniquely associated with this Subsidy.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='openedx_ledger.ledger'),
        ),
        migrations.AlterField(
            model_name='historicalsubsidy',
            name='reference_type',
            field=models.CharField(choices=[('salesforce_opportunity_line_item', 'Salesforce OpportunityLineItem (i.e. Opportunity Product)')], db_index=True, default='salesforce_opportunity_line_item', help_text='The type of object identified by the <code>reference_id</code> field.  Likely to be a type of Salesforce object.', max_length=255),
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='ledger',
            field=models.OneToOneField(blank=True, help_text='The one Ledger uniquely associated with this Subsidy.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='openedx_ledger.ledger'),
        ),
        migrations.AlterField(
            model_name='subsidy',
            name='reference_type',
            field=models.CharField(choices=[('salesforce_opportunity_line_item', 'Salesforce OpportunityLineItem (i.e. Opportunity Product)')], db_index=True, default='salesforce_opportunity_line_item', help_text='The type of object identified by the <code>reference_id</code> field.  Likely to be a type of Salesforce object.', max_length=255),
        ),
    ]
