#!/usr/bin/python3

import os
import xml.dom.minidom as parser

import find_file


def main(start_dir):
    """
    Searches for duplicate dependencies in all pom.xml files in a directory.
    :param start_dir: directory in which to begin the search
    """
    file_sep = os.path.sep
    if not start_dir.endswith(file_sep):
        start_dir = start_dir + file_sep

    paths = find_file.findFile(start_dir, 'pom.xml', recursive=True)
    for p in paths:
        file_duplicates = []
        file_dependencies = find_dependencies(p)
        for dependency_list in file_dependencies:
            duplicates = find_duplicates(dependency_list)
            if duplicates:
                file_duplicates.extend(duplicates)
        if file_duplicates:
            p = p.replace(start_dir, '')
            print('File path: %s' %p)
            print('Duplicates: ')
            for d in file_duplicates:
                print('groupId: ' + d.get('groupId') + '\t\tartifactId: ' + d.get('artifactId') +
                      '\t\tclassifier: ' + str(d.get('classifier')) + '\t\ttype: ' + str(d.get('type')))


def find_dependencies(pomfile):
    """
    Finds dependencies and their ids in a pom.xml file.
    :param pomfile: pom.xml file to be searched
    :return: a list of dependencies elements, each with a list of dependencies and their ids
    """
    doc = parser.parse(pomfile)
    dependencies_elements = doc.getElementsByTagName('dependencies')
    dependencies_ids = []
    for d in dependencies_elements:
        dependencies = d.getElementsByTagName('dependency')
        dependencies_ids.append(find_dependency_ids(dependencies))
    return dependencies_ids


def find_dependency_ids(dependencies):
    """
    Finds dependency groupId, artifactId, type, and classifier attributes.
    :param dependencies: list of dependencies
    :return: a list containing dictionaries representing each dependency
    """
    dependency_list = []
    for d in dependencies:
        dependency = {'groupId': d.getElementsByTagName('groupId')[0].firstChild.data,
                      'artifactId': d.getElementsByTagName('artifactId')[0].firstChild.data}
        classifier = d.getElementsByTagName('classifier')
        dtype = d.getElementsByTagName('type')
        if classifier:
            dependency['classifer'] = classifier[0]
        if dtype:
            dependency['type'] = dtype[0]
        dependency_list.append(dependency)
    return dependency_list


def find_duplicates(dependencies):
    """
    Finds duplicate dependencies in a list of dependencies.
    :param dependencies: a list of dependencies to be checked
    :return: a list of the duplicate dependencies
    """
    duplicates = []
    for d in dependencies:
        if dependencies.count(d) > 1 and duplicates.count(d) == 0:
            duplicates.append(d)
    return duplicates


if __name__ == '__main__':
    root_dir = input("Enter starting directory: ")
    main(root_dir)
