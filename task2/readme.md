## Task 2: USSD + SMS APP
In this challenge I am assuming that the USSD does not have to be live. I used sandbox for USSD but SMS is live. Therefore, use your actual phone number on the emulator so you can receive the confirmation SMS on your phone.

The USSD code is `*384*8959#`.
The live callback URL is: `http://projects.shemkiptoo.com/at/api/ussdsession`.
On the source code the actual logic can be found in the file `task2/app/Http/Controllers/USSDController.php`.

I used laravel framework for the challenge. To run the application:
1. Clone the project.
2. cd into the project root directory.
3. Rename `.env.example` file to `.env` inside your project root and fill the database information. 
4. Run `composer install`
5. Navigate to config/AfricastalkingGateway.php and fill in your username and api_key
6. Run `php artisan migrate`
