import bs4
import requests


def get_ebay_price(product_url):
    r = requests.get(product_url)
    r.raise_for_status()

    soup = bs4.BeautifulSoup(r.text, "html.parser")
    #  Copy 'selector' from right-click inspect on chrome for css path
    elems = soup.select("#mainContent > "
                        "div.vim.d-vi-region.x-atf-center-river--buybox "
                        "> div.vim.x-buybox > div.x-buybox__section > "
                        "div.x-buybox__price-section > div > div.x-bin-price"
                        "__content> div.x-price-primary > span")
    return elems[0].text  # Price of the item

price = get_ebay_price("https://www.ebay.co.uk/itm/143811364887?epid=26046632521&"
                 "hash=item217bd34817:g:IY4AAOSwvaJkoBJN&amdata=enc"
                 "%3AAQAIAAAA8Oh2Q51CqMgM6E57sOb0kmvv76O1uoLes2"
                 "%2BjL6HynyPkvOnaVRSlZx8VTG4iMDmRInJA8bX8yQB3IPBjLGnFEehSzssz"
                 "XzZaKtf2%2Bm9hl%2FNXy0kTFau2rnMFE%2BxRajbrfINkUKMwT%2BPxakLg"
                 "A9GkVzNpIP%2F9uNhbUQHfs9ZPcCD0Pndl4DsTR8NrPFqaAngoKRvkKwJ1uz"
                 "yZq7Zcalj9Fftg%2Be4txH8udMGzTBRPdsqBhPIGrQ87285D%2FGYt8HIRYY"
                 "vFsah0uZ6XOapEAxbNqR7MflZnn0kyWGZ7t5j0WlPgDG1f1oOyH%2FBij4Ho"
                 "%2BCMM%2Bw%3D%3D%7Ctkp%3ABFBM1LbS4uFi")


print("The price is " + price)




