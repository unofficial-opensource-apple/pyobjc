from PyObjCTools.TestSupport import *

from Foundation import *
from AppKit import *
import Foundation

class TestNSAttributedString (TestCase):
    def testOutput(self):
        self.failUnlessArgIsOut(NSAttributedString.attributesAtIndex_effectiveRange_, 1)
        self.failUnlessArgIsOut(NSAttributedString.attribute_atIndex_effectiveRange_, 2)
        self.failUnlessArgIsOut(NSAttributedString.attributesAtIndex_longestEffectiveRange_inRange_, 1)
        self.failUnlessArgIsOut(NSAttributedString.attribute_atIndex_longestEffectiveRange_inRange_, 2)

        self.failUnlessResultIsBOOL(NSAttributedString.isEqualToAttributedString_)

    def testConstantsAppKit(self):
        self.failUnlessIsInstance(NSFontAttributeName, unicode)
        self.failUnlessIsInstance(NSParagraphStyleAttributeName, unicode)
        self.failUnlessIsInstance(NSForegroundColorAttributeName, unicode)
        self.failUnlessIsInstance(NSUnderlineStyleAttributeName, unicode)
        self.failUnlessIsInstance(NSSuperscriptAttributeName, unicode)
        self.failUnlessIsInstance(NSBackgroundColorAttributeName, unicode)
        self.failUnlessIsInstance(NSAttachmentAttributeName, unicode)
        self.failUnlessIsInstance(NSLigatureAttributeName, unicode)
        self.failUnlessIsInstance(NSBaselineOffsetAttributeName, unicode)
        self.failUnlessIsInstance(NSKernAttributeName, unicode)
        self.failUnlessIsInstance(NSLinkAttributeName, unicode)
        self.failUnlessIsInstance(NSStrokeWidthAttributeName, unicode)
        self.failUnlessIsInstance(NSStrokeColorAttributeName, unicode)
        self.failUnlessIsInstance(NSUnderlineColorAttributeName, unicode)
        self.failUnlessIsInstance(NSStrikethroughStyleAttributeName, unicode)
        self.failUnlessIsInstance(NSStrikethroughColorAttributeName, unicode)
        self.failUnlessIsInstance(NSShadowAttributeName, unicode)
        self.failUnlessIsInstance(NSObliquenessAttributeName, unicode)
        self.failUnlessIsInstance(NSExpansionAttributeName, unicode)
        self.failUnlessIsInstance(NSCursorAttributeName, unicode)
        self.failUnlessIsInstance(NSToolTipAttributeName, unicode)
        self.failUnlessIsInstance(NSCharacterShapeAttributeName, unicode)
        self.failUnlessIsInstance(NSGlyphInfoAttributeName, unicode)
        self.failUnlessIsInstance(NSMarkedClauseSegmentAttributeName, unicode)
        self.failUnlessIsInstance(NSSpellingStateAttributeName, unicode)

        self.failUnlessEqual(NSUnderlineStyleNone, 0x00)
        self.failUnlessEqual(NSUnderlineStyleSingle, 0x01)
        self.failUnlessEqual(NSUnderlineStyleThick, 0x02)
        self.failUnlessEqual(NSUnderlineStyleDouble, 0x09)
        self.failUnlessEqual(NSUnderlinePatternSolid, 0x0000)
        self.failUnlessEqual(NSUnderlinePatternDot, 0x0100)
        self.failUnlessEqual(NSUnderlinePatternDash, 0x0200)
        self.failUnlessEqual(NSUnderlinePatternDashDot, 0x0300)
        self.failUnlessEqual(NSUnderlinePatternDashDotDot, 0x0400)

        self.failUnlessEqual(NSSpellingStateSpellingFlag, 1)
        self.failUnlessEqual(NSSpellingStateGrammarFlag, 2)

        self.failUnlessIsInstance(NSPlainTextDocumentType, unicode)
        self.failUnlessIsInstance(NSRTFTextDocumentType, unicode)
        self.failUnlessIsInstance(NSRTFDTextDocumentType, unicode)
        self.failUnlessIsInstance(NSMacSimpleTextDocumentType, unicode)
        self.failUnlessIsInstance(NSHTMLTextDocumentType, unicode)
        self.failUnlessIsInstance(NSDocFormatTextDocumentType, unicode)
        self.failUnlessIsInstance(NSWordMLTextDocumentType, unicode)
        self.failUnlessIsInstance(NSWebArchiveTextDocumentType, unicode)
        self.failUnlessIsInstance(NSOfficeOpenXMLTextDocumentType, unicode)
        self.failUnlessIsInstance(NSOpenDocumentTextDocumentType, unicode)
        self.failUnlessIsInstance(NSPaperSizeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSLeftMarginDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSRightMarginDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSTopMarginDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSBottomMarginDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSViewSizeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSViewZoomDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSViewModeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSDocumentTypeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSReadOnlyDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSConvertedDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSCocoaVersionDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSBackgroundColorDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSHyphenationFactorDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSDefaultTabIntervalDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSCharacterEncodingDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSTitleDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSCompanyDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSCopyrightDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSSubjectDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSAuthorDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSKeywordsDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSCommentDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSEditorDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSCreationTimeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSModificationTimeDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSExcludedElementsDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSTextEncodingNameDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSPrefixSpacesDocumentAttribute, unicode)
        self.failUnlessIsInstance(NSDocumentTypeDocumentOption, unicode)
        self.failUnlessIsInstance(NSDefaultAttributesDocumentOption, unicode)
        self.failUnlessIsInstance(NSCharacterEncodingDocumentOption, unicode)
        self.failUnlessIsInstance(NSTextEncodingNameDocumentOption, unicode)
        self.failUnlessIsInstance(NSBaseURLDocumentOption, unicode)
        self.failUnlessIsInstance(NSTimeoutDocumentOption, unicode)
        self.failUnlessIsInstance(NSWebPreferencesDocumentOption, unicode)
        self.failUnlessIsInstance(NSWebResourceLoadDelegateDocumentOption, unicode)
        self.failUnlessIsInstance(NSTextSizeMultiplierDocumentOption, unicode)

        self.failUnlessEqual(NSNoUnderlineStyle, 0)
        self.failUnlessEqual(NSSingleUnderlineStyle, 1)
        self.failUnlessIsInstance(NSUnderlineStrikethroughMask, (int, long))

    def testMethodsAppKit(self):
        self.failUnlessResultIsBOOL(NSAttributedString.containsAttachments)

        self.failUnlessArgIsOut(NSAttributedString.initWithURL_options_documentAttributes_error_, 2)
        self.failUnlessArgIsOut(NSAttributedString.initWithURL_options_documentAttributes_error_, 3)

        self.failUnlessArgIsOut(NSAttributedString.initWithData_options_documentAttributes_error_, 2)
        self.failUnlessArgIsOut(NSAttributedString.initWithData_options_documentAttributes_error_, 3)

        self.failUnlessArgIsOut(NSAttributedString.initWithPath_documentAttributes_, 1)
        self.failUnlessArgIsOut(NSAttributedString.initWithURL_documentAttributes_, 1)
        self.failUnlessArgIsOut(NSAttributedString.initWithRTF_documentAttributes_, 1)
        self.failUnlessArgIsOut(NSAttributedString.initWithRTFD_documentAttributes_, 1)
        self.failUnlessArgIsOut(NSAttributedString.initWithHTML_documentAttributes_, 1)
        self.failUnlessArgIsOut(NSAttributedString.initWithHTML_baseURL_documentAttributes_, 2)
        self.failUnlessArgIsOut(NSAttributedString.initWithRTFDFileWrapper_documentAttributes_, 1)

        self.failUnlessArgIsOut(NSAttributedString.dataFromRange_documentAttributes_error_, 2)
        self.failUnlessArgIsOut(NSAttributedString.fileWrapperFromRange_documentAttributes_error_, 2)
        
        self.failUnlessResultIsBOOL(NSMutableAttributedString.readFromURL_options_documentAttributes_error_)
        self.failUnlessArgIsOut(NSMutableAttributedString.readFromURL_options_documentAttributes_error_, 2)
        self.failUnlessArgIsOut(NSMutableAttributedString.readFromURL_options_documentAttributes_error_, 3)

        self.failUnlessResultIsBOOL(NSMutableAttributedString.readFromData_options_documentAttributes_error_)
        self.failUnlessArgIsOut(NSMutableAttributedString.readFromData_options_documentAttributes_error_, 2)
        self.failUnlessArgIsOut(NSMutableAttributedString.readFromData_options_documentAttributes_error_, 3)

        self.failUnlessResultIsBOOL(NSMutableAttributedString.readFromURL_options_documentAttributes_)
        self.failUnlessArgIsOut(NSMutableAttributedString.readFromURL_options_documentAttributes_, 2)

        self.failUnlessResultIsBOOL(NSMutableAttributedString.readFromData_options_documentAttributes_)
        self.failUnlessArgIsOut(NSMutableAttributedString.readFromData_options_documentAttributes_, 2)

if __name__ == '__main__':
    main()
