# with pandas this will be not more than 20 rows of code

# inputs

month = input()
stays = int(input())

st_price = 0
ap_price = 0

# decisions
if month == "May" or month == "October":
      st_price = stays * 50
      ap_price = stays * 65
      if 14 >= stays > 7:
            st_price = st_price - st_price * 0.05
      elif stays > 14:
            st_price = st_price - st_price * 0.3
            ap_price = ap_price - ap_price * 0.1

elif month == "June" or month == "September":

      st_price = stays * 75.20
      ap_price = stays * 68.70
      if stays > 14:
            st_price = st_price - st_price * 0.2
            ap_price = ap_price - ap_price * 0.1

else:
      st_price = stays * 76
      ap_price = stays * 77
      if stays > 14:
            ap_price = ap_price - ap_price * 0.1


# output

print(f"Apartment: {ap_price:.2f} lv.\n"
      f"Studio: {st_price:.2f} lv.")
