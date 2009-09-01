# $Id$
# Copyright 2009 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

import objc
from AppKit import *

from dupeguru import app_me_cocoa, scanner

# Fix py2app imports which chokes on relative imports
from dupeguru import app, app_cocoa, data, directories, engine, export, ignore, results, scanner
from hsfs import auto, manual, stats, tree, utils, music
from hsfs.phys import music
from hsmedia import aiff, flac, genres, id3v1, id3v2, mp4, mpeg, ogg, wma

class PyApp(NSObject):
    pass #fake class

class PyDupeGuru(PyApp):
    def init(self):
        self = super(PyDupeGuru,self).init()
        self.app = app_me_cocoa.DupeGuruME()
        return self
    
    #---Directories
    def addDirectory_(self,directory):
        return self.app.add_directory(directory)
    
    def removeDirectory_(self,index):
        self.app.RemoveDirectory(index)
    
    def setDirectory_state_(self,node_path,state):
        self.app.SetDirectoryState(node_path,state)
    
    #---Results
    def clearIgnoreList(self):
        self.app.scanner.ignore_list.Clear()
    
    def doScan(self):
        return self.app.start_scanning()
    
    def exportToXHTMLwithColumns_(self, column_ids):
        return self.app.export_to_xhtml(column_ids)
    
    def loadIgnoreList(self):
        self.app.load_ignore_list()
    
    def loadResults(self):
        self.app.load()
    
    def markAll(self):
        self.app.results.mark_all()
    
    def markNone(self):
        self.app.results.mark_none()
    
    def markInvert(self):
        self.app.results.mark_invert()
    
    def purgeIgnoreList(self):
        self.app.PurgeIgnoreList()
    
    def toggleSelectedMark(self):
        self.app.ToggleSelectedMarkState()
    
    def saveIgnoreList(self):
        self.app.save_ignore_list()
    
    def saveResults(self):
        self.app.save()
    
    def refreshDetailsWithSelected(self):
        self.app.RefreshDetailsWithSelected()
    
    def selectedResultNodePaths(self):
        return self.app.selected_result_node_paths()
    
    def selectResultNodePaths_(self,node_paths):
        self.app.SelectResultNodePaths(node_paths)
    
    def selectedPowerMarkerNodePaths(self):
        return self.app.selected_powermarker_node_paths()
    
    def selectPowerMarkerNodePaths_(self,node_paths):
        self.app.SelectPowerMarkerNodePaths(node_paths)
    
    #---Actions
    def addSelectedToIgnoreList(self):
        self.app.AddSelectedToIgnoreList()
    
    def applyFilter_(self, filter):
        self.app.apply_filter(filter)
    
    def deleteMarked(self):
        self.app.delete_marked()
    
    def makeSelectedReference(self):
        self.app.MakeSelectedReference()
    
    def copyOrMove_markedTo_recreatePath_(self,copy,destination,recreate_path):
        self.app.copy_or_move_marked(copy, destination, recreate_path)
    
    def openSelected(self):
        self.app.OpenSelected()
    
    def removeDeadTracks(self):
        self.app.remove_dead_tracks()
    
    def removeMarked(self):
        self.app.results.perform_on_marked(lambda x:True, True)
    
    def removeSelected(self):
        self.app.RemoveSelected()
    
    def renameSelected_(self,newname):
        return self.app.RenameSelected(newname)
    
    def revealSelected(self):
        self.app.RevealSelected()
    
    def scanDeadTracks(self):
        self.app.scan_dead_tracks()
    
    #---Misc
    def sortDupesBy_ascending_(self,key,asc):
        self.app.sort_dupes(key,asc)
    
    def sortGroupsBy_ascending_(self,key,asc):
        self.app.sort_groups(key,asc)
    
    #---Information
    @objc.signature('i@:')
    def deadTrackCount(self):
        return len(self.app.dead_tracks)
    
    def getIgnoreListCount(self):
        return len(self.app.scanner.ignore_list)
    
    def getMarkCount(self):
        return self.app.results.mark_count
    
    def getStatLine(self):
        return self.app.stat_line
    
    def getOperationalErrorCount(self):
        return self.app.last_op_error_count
    
    #---Data
    @objc.signature('i@:i')
    def getOutlineViewMaxLevel_(self, tag):
        return self.app.GetOutlineViewMaxLevel(tag)
    
    @objc.signature('@@:i@')
    def getOutlineView_childCountsForPath_(self, tag, node_path):
        return self.app.GetOutlineViewChildCounts(tag, node_path)
    
    def getOutlineView_valuesForIndexes_(self,tag,node_path):
        return self.app.GetOutlineViewValues(tag,node_path)
    
    def getOutlineView_markedAtIndexes_(self,tag,node_path):
        return self.app.GetOutlineViewMarked(tag,node_path)
    
    def getTableViewCount_(self,tag):
        return self.app.GetTableViewCount(tag)
    
    def getTableViewMarkedIndexes_(self,tag):
        return self.app.GetTableViewMarkedIndexes(tag)
    
    def getTableView_valuesForRow_(self,tag,row):
        return self.app.GetTableViewValues(tag,row)
    
    #---Properties
    def setMinMatchPercentage_(self, percentage):
        self.app.scanner.min_match_percentage = int(percentage)
    
    def setScanType_(self, scan_type):
        try:
            self.app.scanner.scan_type = [
                scanner.SCAN_TYPE_FILENAME,
                scanner.SCAN_TYPE_FIELDS,
                scanner.SCAN_TYPE_FIELDS_NO_ORDER,
                scanner.SCAN_TYPE_TAG,
                scanner.SCAN_TYPE_CONTENT,
                scanner.SCAN_TYPE_CONTENT_AUDIO
            ][scan_type]
        except IndexError:
            pass
    
    def setWordWeighting_(self, words_are_weighted):
        self.app.scanner.word_weighting = words_are_weighted
    
    def setMixFileKind_(self, mix_file_kind):
        self.app.scanner.mix_file_kind = mix_file_kind
    
    def setDisplayDeltaValues_(self, display_delta_values):
        self.app.display_delta_values = display_delta_values
    
    def setMatchSimilarWords_(self, match_similar_words):
        self.app.scanner.match_similar_words = match_similar_words
    
    def setEscapeFilterRegexp_(self, escape_filter_regexp):
        self.app.options['escape_filter_regexp'] = escape_filter_regexp
    
    def setRemoveEmptyFolders_(self, remove_empty_folders):
        self.app.options['clean_empty_dirs'] = remove_empty_folders
    
    def enable_scanForTag_(self, enable, scan_tag):
        if enable:
            self.app.scanner.scanned_tags.add(scan_tag)
        else:
            self.app.scanner.scanned_tags.discard(scan_tag)
    
    #---Worker
    def getJobProgress(self):
        return self.app.progress.last_progress
    
    def getJobDesc(self):
        return self.app.progress.last_desc
    
    def cancelJob(self):
        self.app.progress.job_cancelled = True
    
    #---Registration
    @objc.signature('i@:')
    def isRegistered(self):
        return self.app.registered
    
    @objc.signature('i@:@@')
    def isCodeValid_withEmail_(self, code, email):
        return self.app.is_code_valid(code, email)
    
    def setRegisteredCode_andEmail_(self, code, email):
        self.app.set_registration(code, email)
    
