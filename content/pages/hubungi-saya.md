---
Title: Hubungi Saya
Slug: hubungi-saya
Status: published
Author: Farrel Franqois
---

<style>
    article input[type="text"], article input[type="email"], article input[type="url"] {
      width: 50%;
      box-sizing: border-box;
      margin-bottom: .75em;
    }

    article textarea {
      width: 50%;
      box-sizing: border-box;
      margin-bottom: .75em;
    }

    label.guide-text {
      color: #AAA;
      margin-left: .25em;
      font-weight: 400;
    }

    article p.hidden {
      display: none;
      visibility: hidden;
      opacity: 0;
    }

    details.info table {
      margin-left:auto; 
      margin-right:auto;
    }
</style>

Jika Anda perlu menghubungi saya secara langsung, bisa langsung Anda mengisi Form Kontak nya di bawah ini. Setelah Anda selesai mengisi nya, maka secara otomatis pesan-pesan tersebut akan di sampaikan langsung oleh Dasbor Netlify saya atau melalui Surel saya, yakni: &lt;farrel(at)franqois(dot)id&gt;

Namun, jika Anda ingin lebih leluasa dalam mengirimkan pesan, seperti menggunakan lampiran dan sebagai nya, bisa Anda langsung kirimkan pesan Anda ke Alamat Surel saya di atas.

## Form Kontak

<form name="contact" class="contact-form" id="contact-form" method="POST" data-netlify="true" netlify-recaptcha="true" netlify-honeypot="required_field">
    <fieldset>
        <p class="hidden">
          <label>Jangan Isikan ini jika Anda adalah manusia: </label><br>
          <input name="required_field" />
        </p>
        <p>
          <label>Nama Anda: </label> <label class="guide-text">(wajib)</label><br>
          <input type="text" name="name" required />
        </p>
        <p>
          <label>Alamat Surel Anda:</label> <label class="guide-text">(wajib)</label><br>
          <input type="email" name="email" required />
        </p>
        <p>
          <label>Alamat URL Situs Web/Blog Anda: <label class="guide-text">(Jika Punya)</label><br>
          <input type="url" name="url" />
        </p>
        <p>
          <label>Pesan: </label> <label class="guide-text">(wajib)</label><br>
          <textarea name="message" rows="5" required></textarea>
        </p>
        <p>
          <label>Persetujuan: </label>
          <p>
            <input type="checkbox" name="terms" value="agree" required> <label>Dengan mencentang dan mengirimkan Informasi ini, maka berarti Anda menyetujui <a href="https://farrel.franqois.id/ketentuan-hukum-dan-sanggahan">ketentuan yang berlaku disini</a></label>
          </p>
          <p>
            <input type="checkbox" name="morality" value="agree" required> <label>Dengan mencentang dan mengirimkan Informasi ini, maka berarti Anda menyetujui segala aturan yang "tidak tertulis" atau tidak saya tulis di blog ini.</label>
          </p>
        </p>
        <div class="g-recaptcha" data-sitekey="6Ldh-TAUAAAAAE468ek0vOM2Mc-BSsKFbA-XkErJ" data-callback="onSubmit">
        </div>
        <p>
          <button type="submit" id="submit">Kirim</button> 
          <button type="reset">Set Ulang Form</button>
        </p>
        <p>
          <label style="font-weight: bold;">Catatan:</label> Formulir ini di proteksi oleh Google reCAPTCHA v2, sebelum melanjutkan, silahkan lihat/baca <a class="p__a" href="https://policies.google.com/privacy" target="_blank" rel="external">Kebijakan Privasi</a> dan <a class="p__a" href="https://policies.google.com/terms" target="_blank" rel="external">Syarat dan Ketentuan nya</a> terlebih dahulu.
        </p>
    </fieldset>
</form>

Saya akan hormati Privasi pada pesan yang Anda sampaikan, karena saya paham betapa pentingnya menjaga data pribadi/privasi Anda, maka **jangan sekali-kali** Anda mengirimkan segala Informasi yang bersifat Rahasia atau/dan Pribadi Anda kepada saya, termasuk No. Telepon, Alamat tempat tinggal, dll ke saya tanpa mengenali nya dan tanpa maksud, alasan dan tujuan yang jelas. 

Kalau Anda mengirimkan nya, maka pesan yang Anda kirimkan akan saya hapus. 

Tapi, jika Informasi yang Anda kirimkan nanti di sebarkan oleh 'pihak ke-3', maka saya tidak akan bisa meng-hapus nya, karena itu sudah berada di luar kendali saya. 

Karena hal itu, sesuai dengan [ketentuan yang berlaku]({filename}/pages/ketentuan-hukum-dan-sanggahan.md) disini, maka saya **tidak akan bertanggung jawab** atas Informasi yang Anda kirimkan kepada saya, jadi apapun Informasi yang telah yang Anda kirimkan ke saya, itu sepenuhnya **tanggung jawab Anda**.

Kecuali jika Anda meng-enkripsi seluruh pesan nya, maka mungkin saja pihak ke-3 tidak dapat melihat/membaca isi pesan yang sebenarnya, sampai ia tahu bagaimana cara men-dekripsi-kan nya.

Jika Anda ingin meng-enkripsi pesan yang ingin Anda sampai, silahkan Enkripsi-kan itu menggunakan Kunci PGP/GPG Publik milik saya, informasi nya sebagai berikut:

**Catatan:** Informasi Kunci PGP/GPG di bawah ini sebaiknya Anda ambil salah satu nya saja, karena sama saja dan di bawah ini merupakan Informasi mengenai 1 Kunci PGP/GPG milik saya saja.

??? info "Informasi Kunci PGP/GPG Publik"
    | Informasi 	| Nilai 	| Tautan 	|
    |:----------:	|:-----------------------------------------------------------:	|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:	|
    | ID Kunci 	| `:::text 0x82721CE49D1B3EB4` 	| [Mailvelope](https://keys.mailvelope.com/pks/lookup?op=get&search=0x82721CE49D1B3EB4), OpenPGP.org ([Cari](https://keys.openpgp.org/search?q=0x82721CE49D1B3EB4) - [Unduh](https://keys.openpgp.org/vks/v1/by-keyid/0x82721CE49D1B3EB4)) 	|
    | Sidik Jari 	| `:::text 709B 5E09 D836 0C6D 75D5 9DA0 8272 1CE4 9D1B 3EB4` 	| OpenPGP.org ([Cari](https://keys.openpgp.org/search?q=709B5E09D8360C6D75D59DA082721CE49D1B3EB4) - [Unduh](https://keys.openpgp.org/vks/v1/by-fingerprint/709B5E09D8360C6D75D59DA082721CE49D1B3EB4)) 	|

Tapi, sebagai gantinya, Anda harus berikan Informasi mengenai Kunci PGP/GPG Publik milik Anda di dalam pesan yang Anda sampaikan, agar saya bisa meng-enkripsikan pesan saya juga.

Saya juga tidak akan memberikan Informasi Pribadi saya kepada Anda, tanpa mengenali nya terlebih dahulu, dan tanpa alasan, maksud dan tujuan yang jelas, bahkan jika Anda minta sekalipun!

Dah, sepertinya itu saja untuk laman kali ini, semoga saya bisa membalas pesan dan Informasi yang telah Anda sampaikan. Dan, salam kenal juga :slightly_smiling_face:

Terima kasih atas perhatian nya :blush:
