"""
Constants and helpers for the KGTK file format.

"""

import sys
import typing

from kgtk.join.validationaction import ValidationAction

class KgtkFormat:
    COLUMN_SEPARATOR: str = "\t"
    COMMENT_INDICATOR: str = "#"
    LIST_SEPARATOR: str = "|"

    # These are the required columns in an edge file:
    NODE1_COLUMN_NAMES: typing.List[str] = ["node1", "from", "subject"]
    NODE2_COLUMN_NAMES: typing.List[str] = ["node2", "to", "object"]
    LABEL_COLUMN_NAMES: typing.List[str] = ["label", "predicate", "relation", "relationship"]

    # There is only one required column in a node file:
    ID_COLUMN_NAMES: typing.List[str] = ["id", "ID"]

    @classmethod
    def _yelp(cls,
              msg: str,
              header_line: str,
              error_action: ValidationAction,
              error_file: typing.TextIO = sys.stderr)->bool:
        """
        Take a validation action.  Only ERROR is special, all other values are treated as EXIT.
        """
        result: bool
        if error_action == ValidationAction.ERROR:
            # Immediately raise an exception.
            raise ValueError("In input header'%s': %s" % (header_line, msg))

        if (error_action in [ValidationAction.REPORT, ValidationAction.COMPLAIN, ValidationAction.EXIT ]):
            print("In input header '%s': %s" % (header_line, msg), file=error_file)
        if error_action == ValidationAction.EXIT:
            sys.exit(1)
        return error_action in [ValidationAction.PASS, ValidationAction.REPORT]

    @classmethod
    def get_column_idx(cls,
                       name_or_aliases: typing.List[str],
                       column_name_map: typing.Mapping[str, int],
                       header_line: str,
                       error_action: ValidationAction,
                       error_file: typing.TextIO = sys.stderr,
                       is_optional: bool = False,
    )->int:
        """
        Get the indices of the required column using one of its allowable names.
        Return -1 if the column is not found and is optional.
        """
        found_column_name: str = ""
        column_idx: int = -1
        col_name: str
        for col_name in name_or_aliases:
            if col_name in column_name_map:
                if column_idx >= 0:
                    cls._yelp("Ambiguous required column names %s and %s" % (found_column_name, col_name),
                              header_line=header_line, error_action=error_action, error_file=error_file)
                column_idx = column_name_map[col_name]
                found_column_name = col_name
        if column_idx < 0 and not is_optional:
            # TODO: throw a better exception:
            cls._yelp("Missing required column: %s" % " | ".join(name_or_aliases),
                      header_line=header_line, error_action=error_action, error_file=error_file)
        return column_idx

    @classmethod
    def check_column_name(cls,
                          column_name: str,
                          header_line: str,
                          error_action: ValidationAction,
                          error_file: typing.TextIO = sys.stderr)->typing.List[str]:
        # Returns a list of complaints.
        # Check for valid column names.
        # 1) Check for leading white space
        # 2) Check for trailing white space
        # 3) Check for internal white space
        #    1) except inside "" and '' quoted strings
        # 4) Check for commas
        # 5) Check for vertical bars
        # 6) Check for semicolons
        #
        # TODO: It might be possible to make some of these checks more efficient.
        results: typing.List[str] = [ ]
        if column_name.lstrip() != column_name:
            results.append("Column name '%s' starts with leading white space" % column_name)
        if column_name.rstrip() != column_name:
            results.append("Column name '%s' ends with leading white space" % column_name)
        if not (column_name.startswith('"') or column_name.startswith("'")):
            if ''.join(column_name.split()) != column_name.strip():
                results.append("Column name '%s' contains internal white space" % column_name)
        if "," in column_name:
            results.append("Column name '%s' contains a comma (,)" % column_name)
        if "|" in column_name:
            results.append("Column name '%s' contains a vertical bar (|)" % column_name)
        if ";" in column_name:
            results.append("Column name '%s' contains a semicolon (;)" % column_name)
        return results
    

    @classmethod
    def check_column_names(cls,
                           column_names: typing.List[str],
                           header_line: str,
                           error_action: ValidationAction,
                           error_file: typing.TextIO = sys.stderr)->bool:
        """
        Returns True if the column names are OK.
        """
        complaints: typing.List[str] = [ ]
        column_name: str
        for column_name in column_names:
            gripes: typing.List[str] = cls.check_column_name(column_name, header_line, error_action, error_file)
            complaints.extend(gripes)
        if len(complaints) == 0:
            return True
        # take the error action, joining the complaints into a single message.
        msg = ", ".join(complaints)
        cls._yelp(msg, header_line=header_line, error_action=error_action, error_file=error_file)
        return False

    @classmethod
    def build_column_name_map(cls,
                              column_names: typing.List[str],
                              header_line: str,
                              error_action: ValidationAction,
                              error_file: typing.TextIO = sys.stderr
    )->typing.Mapping[str, int]:
        # Validate the column names and build a map from column name
        # to column index.
        column_name_map: typing.MutableMapping[str, int] = { }
        column_idx: int = 0 # There may be a more pythonic way to do this
        column_name: str
        for column_name in column_names:
            if column_name is None or len(column_name) == 0:
                cls._yelp("Column %d has an invalid name in the file header" % column_idx,
                          header_line=header_line, error_action=error_action, error_file=error_file)

            # Ensure that columns names are not duplicated:
            if column_name in column_name_map:
               cls._yelp("Column %d (%s) is a duplicate of column %d" % (column_idx, column_name, column_name_map[column_name]),
                         header_line=header_line, error_action=error_action, error_file=error_file)

            column_name_map[column_name] = column_idx
            column_idx += 1
        return column_name_map

    @classmethod
    def required_edge_columns(cls,
                              column_name_map: typing.Mapping[str, int],
                              header_line: str,
                              error_action: ValidationAction,
                              error_file: typing.TextIO = sys.stderr
    )->typing.Tuple[int, int, int]:
        # Ensure that the three required columns are present:
        node1_column_idx: int = cls.get_column_idx(cls.NODE1_COLUMN_NAMES, column_name_map,
                                                   header_line=header_line, error_action=error_action, error_file=error_file)

        node2_column_idx: int = cls.get_column_idx(cls.NODE2_COLUMN_NAMES, column_name_map,
                                                   header_line=header_line, error_action=error_action, error_file=error_file)
                                                   
        label_column_idx: int = cls.get_column_idx(cls.LABEL_COLUMN_NAMES, column_name_map,
                                                   header_line=header_line, error_action=error_action, error_file=error_file)

        return (node1_column_idx, node2_column_idx, label_column_idx)

    @classmethod
    def required_node_column(cls,
                             column_name_map: typing.Mapping[str, int],
                             header_line: str,
                             error_action: ValidationAction,
                             error_file: typing.TextIO = sys.stderr
    )->int:
        # Ensure that the required column is present:
        return cls.get_column_idx(cls.ID_COLUMN_NAMES, column_name_map,
                                  header_line=header_line, error_action=error_action, error_file=error_file)

    @classmethod
    def additional_edge_columns(cls, column_names: typing.List[str])->typing.List[str]:
        """
        Return a list of column names in this file excluding the required columns.
        """
        additional_columns: typing.List[str] = [ ]
        column_name: str
        for column_name in column_names:
            if column_name not in KgtkFormat.NODE1_COLUMN_NAMES and \
               column_name not in KgtkFormat.NODE2_COLUMN_NAMES and \
               column_name not in KgtkFormat.LABEL_COLUMN_NAMES:
                additional_columns.append(column_name)
        return additional_columns

    @classmethod
    def additional_node_columns(cls,
                                column_names: typing.List[str],
    )->typing.List[str]:
        """
        Return a list of column names in this file excluding the required columns.
        """
        additional_columns: typing.List[str] = [ ]
        column_name: str
        for column_name in column_names:
            if column_name not in KgtkFormat.ID_COLUMN_NAMES:
                additional_columns.append(column_name)
        return additional_columns
    
