class PopUpMessages {
    constructor() {
        return this;
    }

    savedSuccessfully() {
        let save_successfull = $.bootstrapGrowl("Saved Successfully", {
            type: 'success',
            align: 'center',
            width: 'auto'
        });
        return save_successfull;
    }

    deletedSuccessfully() {
        let deleted = $.bootstrapGrowl("Deleted Successfully!", {
            type: 'success',
            align: 'center',
            width: 'auto'
        });
        return deleted;
    }

    xhrError(xhr) {
        let xhr_error = $.bootstrapGrowl(xhr.status, {
            type: 'danger',
            align: 'center',
            width: 'auto'
        });
        return xhr_error;
    }

    throwError(thrownError) {
        let throw_error = $.bootstrapGrowl(thrownError, {
            type: 'danger',
            align: 'center',
            width: 'auto'
        });
        return throw_error;
    }

    disabledSuccessfully() {
        let disabled = $.bootstrapGrowl("Disabled Successfully!", {
            type: 'success',
            align: 'center',
            width: 'auto'
        });
        return disabled;
    }

    alreadyDisabled() {
        let disabled = $.bootstrapGrowl("User already disabled", {
            type: 'warning',
            align: 'center',
            width: 'auto'
        });
        return disabled;
    }

}