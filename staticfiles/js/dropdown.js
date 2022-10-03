function drawSelect(data, selectName) {
    $('.' + selectName).select2({
        data: data,
    });
};