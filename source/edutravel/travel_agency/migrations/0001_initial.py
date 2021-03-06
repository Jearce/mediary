# Generated by Django 3.0.5 on 2020-04-15 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('accepted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('booking_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('logitude', models.FloatField()),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('capital', models.CharField(max_length=80)),
                ('currency', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('passport', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_type', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='GradeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('min_credits', models.IntegerField()),
                ('max_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GuideSpecialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industry', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('street_address', models.CharField(max_length=80)),
                ('city_address', models.CharField(max_length=80)),
                ('state_address', models.CharField(max_length=80)),
                ('country_address', models.CharField(max_length=80)),
                ('institute_type', models.CharField(max_length=80)),
                ('student_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstituteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_type', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LocalGuide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('passport', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=12)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.City')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.GuideSpecialty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocalLodging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.City')),
            ],
        ),
        migrations.CreateModel(
            name='LocalTransportation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.City')),
            ],
        ),
        migrations.CreateModel(
            name='Majors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=80)),
                ('number_of_payments', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('passport', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=12)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Institute')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('trip_expense', models.DecimalField(decimal_places=2, max_digits=6)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('destinations', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('entity', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='TripRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Traveler')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Trip')),
            ],
        ),
        migrations.CreateModel(
            name='TripHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('traveler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Traveler')),
            ],
        ),
        migrations.CreateModel(
            name='TripExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateTimeField()),
                ('reason', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.ExpenseType')),
            ],
        ),
        migrations.CreateModel(
            name='TripCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.City')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.LocalGuide')),
                ('lodging', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.LocalLodging')),
                ('transportation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.LocalTransportation')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Trip')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='cities',
            field=models.ManyToManyField(through='travel_agency.TripCity', to='travel_agency.City'),
        ),
        migrations.AddField(
            model_name='trip',
            name='institutes',
            field=models.ManyToManyField(through='travel_agency.Booking', to='travel_agency.Institute'),
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Employee'),
        ),
        migrations.AddField(
            model_name='traveler',
            name='trips',
            field=models.ManyToManyField(through='travel_agency.TripRegistration', to='travel_agency.Trip'),
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('passport', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=12)),
                ('declared_major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Majors')),
                ('grade_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.GradeLevel')),
                ('traveler', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Traveler')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequestForProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('submission_date', models.DateField()),
                ('projected_date', models.DateField()),
                ('rfp_status', models.CharField(max_length=80)),
                ('proposed_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('accepted_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Institute')),
                ('trips', models.ManyToManyField(through='travel_agency.Bid', to='travel_agency.Trip')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_type', models.CharField(max_length=12)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Invoice')),
                ('payment_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Status')),
            ],
        ),
        migrations.AddField(
            model_name='localtransportation',
            name='transport_type',
            field=models.ForeignKey(limit_choices_to={'entity': 'LocalTransportation'}, on_delete=django.db.models.deletion.CASCADE, to='travel_agency.TypeTable'),
        ),
        migrations.AddField(
            model_name='locallodging',
            name='lodging_type',
            field=models.ForeignKey(limit_choices_to={'entity': 'LocalLodging'}, on_delete=django.db.models.deletion.CASCADE, to='travel_agency.TypeTable'),
        ),
        migrations.AddField(
            model_name='locallodging',
            name='zip_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.ZipCode'),
        ),
        migrations.CreateModel(
            name='LocalAttraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('street_address', models.CharField(max_length=80)),
                ('is_active', models.BooleanField(default='true')),
                ('business_type', models.ForeignKey(limit_choices_to={'entity': 'LocalBusiness'}, on_delete=django.db.models.deletion.CASCADE, to='travel_agency.TypeTable')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.City')),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Industry')),
                ('zip_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.ZipCode')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.PaymentPlan'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Status'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Trip'),
        ),
        migrations.CreateModel(
            name='InstituteFaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('passport', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=12)),
                ('title', models.CharField(max_length=80)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Department')),
                ('traveler', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Traveler')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='city',
            name='subdivision',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Subdivision'),
        ),
        migrations.AddField(
            model_name='booking',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Institute'),
        ),
        migrations.AddField(
            model_name='booking',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Trip'),
        ),
        migrations.AddField(
            model_name='bid',
            name='rfp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.RequestForProposal'),
        ),
        migrations.AddField(
            model_name='bid',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.Trip'),
        ),
        migrations.CreateModel(
            name='AttractionDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('local_attraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency.LocalAttraction')),
            ],
        ),
    ]
