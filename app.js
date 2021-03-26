function DocAppScript() {
    var doc = DocumentApp.create("Test");
    var footer = doc.addFooter();

    var image = UrlFetchApp.fetch("cat.jpg");
    footer.appendImage(image.getBlob());
}