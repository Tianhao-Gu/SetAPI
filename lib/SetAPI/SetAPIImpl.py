# -*- coding: utf-8 -*-
#BEGIN_HEADER
#END_HEADER


class SetAPI:
    '''
    Module Name:
    SetAPI

    Module Description:
    
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""
    
    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass
    

    def get_reads_set_v1(self, ctx, params):
        """
        :param params: instance of type "GetReadsSetV1Params" (ref -
           workspace reference to ReadsGroup object. include_item_info - 1 or
           0, if 1 additionally provides workspace info (with metadata) for
           each Reads object in the Set) -> structure: parameter "ref" of
           String, parameter "include_item_info" of type "boolean" (A
           boolean. 0 = false, 1 = true.), parameter "ref_path_to_set" of
           list of String
        :returns: instance of type "GetReadsSetV1Result" -> structure:
           parameter "data" of type "ReadsSet" (@meta ws description as
           description @meta ws length(items) as item_count) -> structure:
           parameter "description" of String, parameter "items" of list of
           type "ReadsSetItem" (When saving a ReadsSet, only 'ref' is
           required.  You should never set 'info'.  'info' is provided
           optionally when fetching the ReadsSet.) -> structure: parameter
           "ref" of type "ws_reads_id" (The workspace ID for a Reads data
           object. @id ws KBaseFile.PairedEndLibrary
           KBaseFile.SingleEndLibrary), parameter "label" of String,
           parameter "data_attachments" of list of type "DataAttachment" ->
           structure: parameter "name" of String, parameter "ref" of type
           "ws_obj_id" (The workspace ID for a any data object. @id ws),
           parameter "info" of type "object_info" (Information about an
           object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_reads_set_v1
        #END get_reads_set_v1

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_reads_set_v1 return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def save_reads_set_v1(self, ctx, params):
        """
        :param params: instance of type "SaveReadsSetV1Params"
           (workspace_name or workspace_id - alternative options defining
           target workspace, output_object_name - workspace object name (this
           parameter is used together with one of workspace params from
           above), output_ref - optional workspace reference to ReadsGroup
           object (alternative to previous params, this way is preferable
           when group object already exists and saving operation overrides
           it).) -> structure: parameter "workspace_name" of String,
           parameter "workspace_id" of Long, parameter "output_object_name"
           of String, parameter "output_ref" of String, parameter "data" of
           type "ReadsSet" (@meta ws description as description @meta ws
           length(items) as item_count) -> structure: parameter "description"
           of String, parameter "items" of list of type "ReadsSetItem" (When
           saving a ReadsSet, only 'ref' is required.  You should never set
           'info'.  'info' is provided optionally when fetching the
           ReadsSet.) -> structure: parameter "ref" of type "ws_reads_id"
           (The workspace ID for a Reads data object. @id ws
           KBaseFile.PairedEndLibrary KBaseFile.SingleEndLibrary), parameter
           "label" of String, parameter "data_attachments" of list of type
           "DataAttachment" -> structure: parameter "name" of String,
           parameter "ref" of type "ws_obj_id" (The workspace ID for a any
           data object. @id ws), parameter "info" of type "object_info"
           (Information about an object, including user provided metadata.
           obj_id objid - the numerical id of the object. obj_name name - the
           name of the object. type_string type - the type of the object.
           timestamp save_date - the save date of the object. obj_ver ver -
           the version of the object. username saved_by - the user that saved
           or copied the object. ws_id wsid - the workspace containing the
           object. ws_name workspace - the workspace containing the object.
           string chsum - the md5 checksum of the object. int size - the size
           of the object in bytes. usermeta meta - arbitrary user-supplied
           metadata about the object.) -> tuple of size 11: parameter "objid"
           of type "obj_id" (The unique, permanent numerical ID of an
           object.), parameter "name" of type "obj_name" (A string used as a
           name for an object. Any string consisting of alphanumeric
           characters and the characters |._- that is not an integer is
           acceptable.), parameter "type" of type "type_string" (A type
           string. Specifies the type and its version in a single string in
           the format [module].[typename]-[major].[minor]: module - a string.
           The module name of the typespec containing the type. typename - a
           string. The name of the type as assigned by the typedef statement.
           major - an integer. The major version of the type. A change in the
           major version implies the type has changed in a non-backwards
           compatible way. minor - an integer. The minor version of the type.
           A change in the minor version implies that the type has changed in
           a way that is backwards compatible with previous type definitions.
           In many cases, the major and minor versions are optional, and if
           not provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        :returns: instance of type "SaveReadsSetV1Result" -> structure:
           parameter "set_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN save_reads_set_v1
        #END save_reads_set_v1

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method save_reads_set_v1 return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION, 
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
