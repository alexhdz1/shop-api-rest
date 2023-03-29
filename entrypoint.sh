echo "Running migrations"
# Apply database migrations
python manage.py migrate

# Collect static files
echo "Running collectstatic"
python manage.py collectstatic --noinput

exec "$@"
