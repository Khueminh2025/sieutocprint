#!/usr/bin/env bash
# Build script for Render

# Cài các thư viện
pip install -r requirements.txt

# Thu thập static files
python manage.py collectstatic --no-input

# Di chuyển dữ liệu
python manage.py migrate

# Tạo superuser (chỉ chạy nếu chưa tồn tại)
python manage.py createsuperuser \
  --noinput \
  --username $DJANGO_SUPERUSER_USERNAME \
  --email $DJANGO_SUPERUSER_EMAIL || true
