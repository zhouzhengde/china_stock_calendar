# china_stock_calendar

### How to use
- config csv data, copy data file to /Users/[Your home]/[data folder]/zipline-data-bundle/daily

    ```
        /Users/[Your home]/
                    |-- zipline-data-bundle
                            |- daily
                                    |-- xxxx.csv
                                    |-- yyyy.csv
    ```

- modify /Users/[Your home]/.zipline/extension.py, the content like this:

    ```
        import pandas as pd
        from zipline.data.bundles import register
        from zipline.data.bundles.csvdir import csvdir_equities
        from china_stock_calendar.zipline.default_calendar import shsz_calendar

        start_session = pd.Timestamp('2018-04-12', tz='utc')
        end_session = pd.Timestamp('2019-04-12', tz='utc')

        register(
            'china-test-bundle',
            csvdir_equities(
                ['daily'],
                '/Users/[Your home]/[data folder]/zipline-data-bundle',
            ),
            calendar_name='SHSZ', # config china calendar that named SHSZ
            start_session=start_session,
            end_session=end_session
        )
    ```

- run to generate bundle

    ```
        cd ~/.zipline/
        zipline ingest -b china-test-bundle
    ```

### commonly issue
- TODO

