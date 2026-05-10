pub mod config;
pub mod constants;
pub mod errors;

pub mod package_1;
pub mod package_2;

use crate::package_1::module_A;

pub fn init() {
    println!("initializing app...");
    config::load();
    println!("{}", config::app_name());

    let msg = module_A::hello();
    println!("{}", msg);
}