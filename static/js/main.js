// Динамическое обновление категорий
function updateCategories() {
    const typeId = $("#id_type").val();
    if (typeId) {
        $.get(`/load-categories/?type_id=${typeId}`, function(data) {
            $("#id_category").html(data);
        });
    }
}

// Динамическое обновление подкатегорий
function updateSubcategories() {
    const categoryId = $("#id_category").val();
    if (categoryId) {
        $.get(`/load-subcategories/?category_id=${categoryId}`, function(data) {
            $("#id_subcategory").html(data);
        });
    }
}

$(document).ready(function(){
    $("#id_type").change(updateCategories);
    $("#id_category").change(updateSubcategories);
    
    // Инициализация при загрузке
    updateCategories();
    updateSubcategories();
});