def any_arrows(arrows):
    return any(not arrow.get("damaged",False) for arrow in arrows)


'''
You need to verify that you have some good ones left, in order to prepare for battle:

anyArrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}])
If an arrow in the quiver does not have a damaged status, it means it's new.

The expected result is a boolean, indicating whether you have any good arrows left.

'''