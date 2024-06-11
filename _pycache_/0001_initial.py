class Migration(migrations.Migration):
    initial = True

    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name="Category".
            fields = [
        ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
        ("name", models.CharField(max_length=50)),
    ],
    ),
    migrations.CreateModel(
        name="Customer",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("first_name", models.CharField(max_length=50)),
            ("last_name", models.CharField(max_length=50)),
            ("phone", models.CharField(max_length=20)),
            ("email", models.EmailField(max_length=100)),
            ("password", models.CharField(max_length=100)),
        ],
    ),
    migrations.CreateModel(
        name="Order".
        fields = [
        ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="")
        ("quantity", models.IntegerField(default=1))
        ("address", models.CharField(max_length=100, default="", blank=True, default=True)
        ("phone", models.CharField(max_length=20, default="", blank=True)
        ("date", models.DateField(default=datetime.datetime.today))
        ("status", models.BooleanField(default=False))
        ("customer", models.ForeignKey(on_delete=models.CASCADE, default=1, to="store.Customer")
        ("product", mdoels.ForeignKey(on_delete=models.CASCADE, default=1, to="store.Product")
         ]
         )
    ]