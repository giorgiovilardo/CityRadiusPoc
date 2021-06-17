# City distance poc tool

Just a PoC to explore spatial data

## Usage

* `git clone`
* `docker compose build`
* `docker compose up -d`
* `docker exec -it city-distance-poc-py bash`
* at bash prompt, `./launch.sh`
    * it will seed postgis after fetching all cities from MM api
    * then will throw you in the main loop for the console app
    * use `ctrl+c` to exit the main loop, then `exit` to get out of bash
* **REMEMBER TO `docker compose down` IN ORDER TO KILL THE DB AND RESET IT**    

## Immediately apparent issues

* Cross country "poisoning", need some weights?
