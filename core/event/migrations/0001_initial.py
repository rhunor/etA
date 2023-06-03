# Generated by Django 4.0.10 on 2023-02-23 23:18

import ckeditor_uploader.fields
import core.event.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of Event', max_length=255, verbose_name='Event name')),
                ('slug', models.SlugField(blank=True, help_text='Click on the title field to populate this field', max_length=100, unique=True)),
                ('event_id', models.CharField(db_index=True, default=core.event.models.generate_event_id, max_length=15, verbose_name='Event UUID')),
                ('event_type', models.CharField(choices=[('single', 'Single'), ('recurring', 'Recurring')], default='single', max_length=50, verbose_name='Event Type')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, default='events/cover/default.jpg', help_text='Upload Event Image', null=True, upload_to='events/cover/', verbose_name='Event Image')),
                ('venue', models.CharField(help_text='Enter the location of the Event', max_length=255, verbose_name='Event Venue')),
                ('host', models.CharField(help_text='Enter the Host of the Event', max_length=255, verbose_name='Event Host/Organizer')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active Status')),
                ('publish_status', models.BooleanField(default=False, help_text='Select to Publish Event', verbose_name='Publish Status')),
                ('start_date', models.DateTimeField(verbose_name='Event Start Date')),
                ('end_date', models.DateTimeField(verbose_name='Event End Date')),
                ('website', models.CharField(blank=True, help_text='Optional', max_length=200, null=True, verbose_name='Website')),
                ('instagram', models.CharField(blank=True, help_text='Optional', max_length=200, null=True, verbose_name='Instagram Page')),
                ('facebook', models.CharField(blank=True, help_text='Optional', max_length=200, null=True, verbose_name='Facebook Page')),
                ('twitter', models.CharField(blank=True, help_text='Optional', max_length=200, null=True, verbose_name='Twitter Page')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the new category', max_length=255, unique=True, verbose_name='Category name')),
                ('slug', models.SlugField(unique=True)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, default='events/category/default.jpg', help_text='Upload Category Image', null=True, upload_to='events/category/', verbose_name='Category Image')),
                ('is_active', models.BooleanField(default=True, help_text='Select to make category active')),
            ],
            options={
                'verbose_name': 'Event Category',
                'verbose_name_plural': 'Event Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Ticket name', max_length=50, verbose_name='Ticket name')),
                ('ticket_id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('slug', models.SlugField(help_text='Click on the title field to populate this field')),
                ('type', models.CharField(choices=[('free', 'Free'), ('paid', 'Paid')], default='free', max_length=50, verbose_name='Ticket Type')),
                ('description', models.TextField(max_length=255, verbose_name='Ticket Description')),
                ('is_active', models.BooleanField(default=True, help_text='Select to make ticket active', verbose_name='Ticket Status')),
                ('stock_type', models.CharField(choices=[('limited', 'Limited'), ('unlimited', 'Unlimited')], default='unlimited', max_length=50, verbose_name='Stock Type')),
                ('quantity', models.PositiveIntegerField(blank=True, null=True, verbose_name='Stock Quantity')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Ticket Price')),
                ('limit', models.PositiveSmallIntegerField(default=5, help_text='Max number of tickets purchasable by one person', verbose_name='Purchase Limit')),
                ('charges', models.CharField(choices=[('host', 'Host'), ('guest', 'Guest')], default='host', help_text='Select who bears the charges', max_length=50, verbose_name='Service charges')),
                ('sale_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Ticket Sale Start Date')),
                ('sale_end_date', models.DateTimeField(verbose_name='Ticket Sale End Date')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='event.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.eventcategory'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
