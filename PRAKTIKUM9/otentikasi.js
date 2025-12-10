function cekLogin() {
  const user = document.getElementById("username").value;
  const pass = document.getElementById("password").value;

  const validUser = "ahmad2017";
  const validPass = "integrity";

  if (user === validUser && pass === validPass) {
    alert("Login sukses!");
    window.location.href = "sukses.html";
  } else {
    alert("Login gagal! Username atau password salah.");
  }
}