if [ -f .env ]; then
  mv -f .env .env.$(date -u +%Y%m%d)
else
  echo ".env file does not exist. It will be created."
fi

RANDOM_PASSWORD=$(openssl rand -base64 12)
POSTGRES_PASSWORD=$(python3 -c "import crypt; print(crypt.crypt('$RANDOM_PASSWORD', crypt.mksalt(crypt.METHOD_SHA512)))")
POSTGRES_USER=flask
POSTGRES_DB=blog
FLASK_APP=app.py
DATABASE=postgres
cat > .env <<EOF
DATABASE=${DATABASE}
POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
POSTGRES_USER=${POSTGRES_USER}
POSTGRES_DB=${POSTGRES_DB}
FLASK_APP=${FLASK_APP}
EOF
