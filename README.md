# Fetch Take Home

## How To Run

Just run `./start.sh`.

## What It'll Do

It *should* build an image, use the image to run unit tests, then use the same
image to run `app.py`.  From there the service should be reachable at:
http://127.0.0.1:8000/docs

## Troubleshooting

If it doesn't JustWork™, then you likely need to install or update and configure
Docker.  

## Validating

If you'd like to you can run `tests/e2e_tests.py` to make sure the app is doing
what is expected of it.  The script requires the `requests` library.  None of
the code in this repo should install anything outside of a docker image, so you
will have to ensure `requests` is present.

## Additional Info

* This app uses the Python FastAPI framework on top of Python 3.13
* There has been considerable effort to keep the code as DRY as possible
* The Receipt model does not include `id` field itself, by choice
* The ReceiptScorer makes heavy use of comprehension and ternaries for brevity
* There should be no broken tests or deprication warnings
* Receipts are stored in memory, but still serializes and deserializes for
  storage and retrieval
* To follow the spec provided UUID4s are presented with the dashes ("-") in the
  presentation, but for storage the keys omit them
* Imports are ordered by:
    * First by standard library, 3rd party libraries, and internal libraries
    * Within each block direct imports, then imports from
    * Within each grouping they are alphabetized
* There can always be more tests
