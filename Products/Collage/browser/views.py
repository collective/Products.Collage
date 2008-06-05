from Products.Five.browser import BrowserView

from Products.CMFCore.utils import getToolByName

class BaseView(BrowserView):
    def test(self):
        return lambda a, b, c: a and b or c

    def isAnon(self):
        return getToolByName(self.context, 'portal_membership').isAnonymousUser()

    def normalizeString(self):
        return getToolByName(self.context, 'plone_utils').normalizeString

    def mtool(self):
        return getToolByName(self.context, 'portal_membership')

    def portal_url(self):
        return getToolByName(self.context, 'portal_url')()

    def site_properties(self):
        props = getToolByName(self.context, 'portal_properties')
        return props.site_properties
    
class RowView(BaseView):
    def getColumnBatches(self, bsize=3):
        columns = self.context.folderlistingFolderContents()
        if not columns:
            return []

        # calculate number of batches
        count = (len(columns)-1)/3+1
        
        batches = []
        for c in range(count):
            batch = []
            for i in range(bsize):
                index = c*bsize+i

                # pad with null-columns
                column = None

                if index < len(columns):
                    column = columns[index]

                # do not pad first row
                if column or c > 0:
                    batch += [column]
                
            batches += [batch]
        
        return batches
