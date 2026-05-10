// Configuration to read the .env file automatically
use std::env;

pub fn load() {
    dotenvy::dotenv().ok();
}

pub fn app_name() -> String {
    env::var("APP_NAME").unwrap_or("default_app".to_string())
}

pub fn db_url() -> String {
    env::var("DATABASE_URL").expect("DATABASE_URL no definida")
}