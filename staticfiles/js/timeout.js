
  setTimeout(function() {
    document.querySelectorAll('.message').forEach(function(msg) {
      msg.style.opacity = '0';
      setTimeout(() => msg.style.display = 'none', 500);
    });
  }, 3000);
