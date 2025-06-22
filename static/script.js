function copyToClipboard() {
    const input = document.getElementById('shortUrl');
    navigator.clipboard.writeText(input.value).then(() => {
        const toast = document.getElementById('copyMsg');
        toast.style.display = "block";
        setTimeout(() => { toast.style.display = "none"; }, 1500);
    });
}
