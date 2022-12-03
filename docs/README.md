# Workflow - tor_pages.py

[![](https://mermaid.ink/img/pako:eNqNkk1qwzAQha8yaNNFkwt4EchfaaElwU4pFG8m0jgRsSVVkhtKyN0rWzZJ6lLqlfxm3qeZh06Ma0EsYY4-alKcFhJ3FqtcQfgMWi-5NKg8rNPVfJllw8JiupnOptlyWJmlq7dsmQ4L2fpp0eix0pHHk8l9z0rggTzfA0IpnQddwGv67KCwugK_J7grpTrcgcdtSRHSO8cBM-6ICaTka6tc67HEtRUutpdaG8i4RSPVLkrXozSzdNMnMMeyjIit1UdHFrwGbUi1Whjs4u88rT8ueW13RoroNlZzclF93LxcEaIrAIZLGNwRcK08hQhRiR_p_LrFJdAMPyle2COCr52qSYFEi78wYkDBc7vgn_imFQpdK_Ffg6USvdTK7aWBLfkjhVRvl6GeFg5sxCqyFUoRXuypkXMWVqgoZ0k4CrSHnOXqHPqw9jr7Upwl3tY0YrUR6PvXzZICSxfU8Brfte7_z98DTPB3?type=png)](https://mermaid.live/edit#pako:eNqNkk1qwzAQha8yaNNFkwt4EchfaaElwU4pFG8m0jgRsSVVkhtKyN0rWzZJ6lLqlfxm3qeZh06Ma0EsYY4-alKcFhJ3FqtcQfgMWi-5NKg8rNPVfJllw8JiupnOptlyWJmlq7dsmQ4L2fpp0eix0pHHk8l9z0rggTzfA0IpnQddwGv67KCwugK_J7grpTrcgcdtSRHSO8cBM-6ICaTka6tc67HEtRUutpdaG8i4RSPVLkrXozSzdNMnMMeyjIit1UdHFrwGbUi1Whjs4u88rT8ueW13RoroNlZzclF93LxcEaIrAIZLGNwRcK08hQhRiR_p_LrFJdAMPyle2COCr52qSYFEi78wYkDBc7vgn_imFQpdK_Ffg6USvdTK7aWBLfkjhVRvl6GeFg5sxCqyFUoRXuypkXMWVqgoZ0k4CrSHnOXqHPqw9jr7Upwl3tY0YrUR6PvXzZICSxfU8Brfte7_z98DTPB3)


<details>
  <summary>Code - Mermaid</summary><p>

```sequenceDiagram
    participant PROCESS
    participant DATABASE
    participant BROWSER
    participant SPIDER

    PROCESS->>+DATABASE: Fetch a list of URLs from the 'link' table
    DATABASE-->>-PROCESS: Returns the records
    loop Scraping
        PROCESS-->>+BROWSER: Calls the browser to open the URL
        BROWSER-->>+SPIDER: Calls the spider to process the HTML
        SPIDER-->-PROCESS: Returns page content and a list of URLs
        PROCESS-->>DATABASE: Saves the content of the scraped page
        loop Save URL
            PROCESS-->>DATABASE: Save URL found
            PROCESS-->>DATABASE: Save relationship between URLs
        end
    end
```
</details>

<hr>