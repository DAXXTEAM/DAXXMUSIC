from pyrogram import Client, filters
import random
from DAXXMUSIC import app
from pyrogram.types import InputMediaVideo


NUDE = [
          "https://te.legra.ph/file/0ca5e90b88d4fb8eef549.jpg",
          "https://te.legra.ph/file/6278eff353887daddebb2.jpg",
          "https://graph.org/file/dd585189ffd3a4235f4a6.jpg",
          "https://graph.org/file/66674a8a82bfdea946849.jpg",
          "https://graph.org/file/e6191cb260b1e37e7d4d5.jpg",
          "https://graph.org/file/5500df4f42b55c22bb644.jpg",
          "https://graph.org/file/d91436f1e26a596d7ec6e.jpg",
          "https://graph.og/file/4f474f24fbc5984e9535e.jpg",
          "https://graph.org/file/b11698ff09758f1419c21.jpg",
          "https://graph.org/file/c1f6a80bdf5c88c894341.jpg",
          "https://graph.org/file/088a7154389742f8408d4.jpg",
          "https://graph.org/file/5605e7d70fbb129373f5a.jpg",
          "https://graph.org/file/94cf471de65d23ceb7970.jpg",
          "https://graph.org/file/87ccac3096c1352f1e479.jpg",
          "https://graph.org/file/5453aa234a167895cc2aa.jpg",
          "https://graph.org/file/a9f6b570a62e2652e4b25.jpg",
          "https://graph.org/file/c4502806d6812b3e358f9.jpg",
          "https://graph.org/file/6ff10a6598ab8f2b93b85.jpg",
          "https://graph.org/file/a60b1d15700794b81176f.jpg",
          "https://graph.org/file/99851fe3adcb6fed95144.jpg",
          "https://graph.org/file/51c2162407d7c3ee5fd1d.jpg",
          "https://graph.org/file/3c49e94613fa521c43b23.jpg",
          "https://graph.org/file/92ff8235464bae00969be.jpg",
          "https://graph.org/file/2965a4e0acee2b8809aa9.jpg",
          "https://graph.org/file/faa350b61d7477fe7caa3.jpg",
          "https://graph.org/file/d074ae3453b9bfb86ff5c.jpg",
          "https://graph.org/file/41fb44ca09cef382e0cca.jpg",
          "https://graph.org/file/a46a5f01ffabc1cb60b58.jpg",
          "https://graph.org/file/3ebe28b1499b0950adb5d.jpg",
          "https://graph.org/file/291ae4ca58eea370042a5.jpg",
          "https://graph.org/file/834dea05eb803abe7ba34.jpg",
          "https://graph.org/file/3634d9ad192c418077912.jpg",
          "https://graph.org/file/beb529ae5d7d8a5aa224f.jpg",
          "https://graph.org/file/10aef6c9d02a35a03c0f9.jpg",
          "https://graph.org/file/f3348aadab3f52485734f.jpg",
          "https://graph.org/file/b6446e30f1a52ee45fdad.jpg",
          "https://graph.org/file/808497f62b3cdaf81005b.jpg",
          "https://graph.org/file/a052438e354d703fd684d.jpg",
          "https://graph.org/file/589203cab2af2627d1dc2.jpg",
          "https://graph.org/file/54ae0961b204ec76495b6.jpg",
          "https://graph.org/file/db6c256958bcdd37aa037.jpg",
          "https://graph.org/file/752137643c3e712270fdc.jpg",
          "https://graph.org/file/14203c880c8b11c0adc9a.jpg",
          "https://graph.org/file/7ebc34698bfa1d586a7f6.jpg",
          "https://graph.org/file/5655efc66810592e6c604.jpg",
          "https://graph.org/file/e576103c0998477fdf297.jpg",
          "https://graph.org/file/e576103c0998477fdf297.jpg",
          "https://graph.org/file/17857d752288d1045e080.jpg",
          "https://graph.org/file/f44c47d8f054b879815c8.jpg",
          "https://graph.org/file/24f29bde75317c21b1495.jpg",
          "https://graph.org/file/4ad8b51bb10e38e2c35d2.jpg",
          "https://graph.org/file/389bedd6f364d199178a4.jpg",
          "https://graph.org/file/ad4d5e8cecfe4514b8864.jpg",
          "https://graph.org/file/aa2706a3adef6157b9635.jpg",
          "https://graph.org/file/8b076842455540ff87cf4.jpg",
]

NUDES_GIF = ["https://te.legra.ph/file/f1b40793c472c5db8d87a.mp4",
            "https://te.legra.ph/file/ba12f5dcd06fd9f416b90.mp4",
            "https://te.legra.ph/file/f0b5f300c3eb2fae90385.mp4",
            "https://te.legra.ph/file/a227c13605ff01c3f2014.mp4",
            "https://te.legra.ph/file/380080d9938a406892cb7.mp4",
            "https://te.legra.ph/file/a512c31e95175520d0331.mp4",
            "https://te.legra.ph/file/d295649fd9471f4092424.mp4",
            "https://te.legra.ph/file/3a1752f79472f0648dd7e.mp4",
            "https://te.legra.ph/file/4479037a28947ba1d0249.mp4",
            "https://te.legra.ph/file/6b13339486ab6c8c83df6.mp4",
            "https://te.legra.ph/file/cc7c1822ea498ececf65a.mp4",
            "https://te.legra.ph/file/a882421970e7f600e8d3c.mp4",
            "https://te.legra.ph/file/aa02149a462f6f8495e8a.mp4",
            "https://te.legra.ph/file/90765abc4200b7f28d41f.mp4",
            "https://te.legra.ph/file/4be9400898d497a6dee09.mp4",
            "https://te.legra.ph/file/4be9400898d497a6dee09.mp4",
            "https://te.legra.ph/file/fe1e7cb3d6a60e4285cb0.mp4",
            "https://te.legra.ph/file/1bd5c94482d7a82210a25.mp4",
            "https://te.legra.ph/file/1bd5c94482d7a82210a25.mp4",
            "https://te.legra.ph/file/bb934e0d1344c9a005d4d.mp4",
            "https://te.legra.ph/file/0021efe61fee2505ea590.mp4",
            "https://te.legra.ph/file/7e7924665d58d55f627fd.mp4",
            "https://te.legra.ph/file/b914497b31b3dba446f18.mp4",
            "https://te.legra.ph/file/5596d6e58c2074640caae.mp4",
            "https://te.legra.ph/file/47c7e73d18770908d974d.mp4",
            "https://te.legra.ph/file/172b83d8f950683da6032.mp4",
            "https://te.legra.ph/file/a4ec1a5bf30542ab8fbe7.mp4",
            "https://te.legra.ph/file/34ffd6b5b3655decbd0f0.mp4",
            "https://te.legra.ph/file/0a188dd176ef6f71fb326.mp4",
            "https://te.legra.ph/file/dd2973840778992d3597b.mp4",
            "https://te.legra.ph/file/f01ee4b92041fa3c8e8f1.mp4",
            "https://te.legra.ph/file/afda53ee167b94e05e1f5.mp4",
            "https://te.legra.ph/file/9434bab455cac1a0d8c70.mp4",
            "https://te.legra.ph/file/9434bab455cac1a0d8c70.mp4",
            "https://te.legra.ph/file/12b185cb776971ebd7d12.mp4",
            "https://te.legra.ph/file/6a776551ed6ceffb82026.mp4",
            "https://te.legra.ph/file/6d47ec45a550cb684eca0.mp4",
            "https://te.legra.ph/file/de14f21d4bc34896e0f3c.mp4",
            "https://te.legra.ph/file/f9bc24ead72f358f43c86.mp4",
            "https://te.legra.ph/file/0959d3d607698cc3fb66e.mp4",
            "https://te.legra.ph/file/0d024c670bc61b264b51a.mp4",
            "https://te.legra.ph/file/b0640a58b1d1899b56124.mp4",
            "https://te.legra.ph/file/88ff6ad6e88e2224de57e.mp4",
            "https://te.legra.ph/file/9cdb4cc983c2ca35d54a4.mp4",
            "https://te.legra.ph/file/fb184b5fe923ca688d969.mp4",
            "https://te.legra.ph/file/b316c7bf81cf4da687a0f.mp4",
            "https://te.legra.ph/file/9bed217ac9c2d714cb6ed.mp4",
            "https://te.legra.ph/file/a3858d196f3a656630f98.mp4",
            "https://te.legra.ph/file/9bed217ac9c2d714cb6ed.mp4",
            "https://te.legra.ph/file/4d5cf207993f27a95ba13.mp4" ]
            
            
            
            
@app.on_message(filters.command(["nude"]))
def send_nude(_, message):
    random_nude = random.choice(NUDE)
    message.reply_photo(random_nude)


@app.on_message(filters.command(["ngif"]))
def send_nude_gif(_, message):
    random_nude_gif = random.choice(NUDES_GIF)
    message.reply_video(random_nude_gif)
    
                            